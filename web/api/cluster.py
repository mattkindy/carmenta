from flask import Blueprint, request

from api.api import api_root
from selenium import webdriver
from api.scrape import linkedin_login
from scraper.interface.candidate import Candidate
from clustering.knn_probability import KNNProbabilityCalculator
from clustering.similarity import similarity_metric, candidates_to_metrics
import json

cluster_root = Blueprint('cluster', __name__, url_prefix="{}/cluster".format(api_root.url_prefix))


@cluster_root.route('/', methods=['POST'])
def recalculate_clustering():
  # get user resource

  data = request.get_json()
  username = data["username"]
  password = data["password"]
  link = data["link"]

  # person to do comparison on
  driver = webdriver.Chrome()
  linkedin_login(driver, username, password)
  print('Scraping: {}'.format(link))
  candidate = Candidate(link, driver=driver, scrape=False)
  candidate.scrape(close_on_complete=False)

  experience = candidate.experiences[0] if candidate.experiences else None
  education = candidate.educations[0] if candidate.educations else None

  entry = [{
    'name': candidate.name,
    'job_title': experience.position_title if experience else None,
    'company': experience.institution_name if experience else None,
    'college': education.institution_name if education else None,
    'location': experience.location if experience else None,
  }]

  seed1 = []
  labels1 = []
  with open('../files/praetorian.txt','r') as f:
    candidates_good = json.load(f)
    seed1 = candidates_to_metrics(candidates_good)
  seed2 = []
  labels1 = [0]*len(seed1)
  with open('../files/known_bad.txt', 'r') as f:
    candidates_bad = json.load(f)
    seed2 = candidates_to_metrics(candidates_bad)
  seed1.extend(seed2)
  labels1.extend([1]*len(seed2))
  all_users = candidates_to_metrics(entry)
  print(seed1)
  print(labels1)
  probability_calculator = KNNProbabilityCalculator(seed1,
                                                    labels1,
                                                    similarity_fn=similarity_metric)

  ret = []
  for (user, probability) in zip(all_users, probability_calculator.probability(all_users)):
    # update db for user probability
    ret.append({"user":link, "prob":probability})

  return json.dumps(ret)