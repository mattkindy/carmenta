from flask import Blueprint

from api.api import api_root
from clustering.knn_probability import KNNProbabilityCalculator
from clustering.similarity import similarity_metric, candidates_to_metrics
import json
import request

cluster_root = Blueprint('cluster', __name__, url_prefix="{}/cluster".format(api_root.url_prefix))


@cluster_root.route('/', methods=['POST'])
def recalculate_clustering():
  # get user resource
  #TODO change this

  seed1 = []
  labels1 = []
  with open('../files/praetorian.txt','r') as f:
    candidates_good = json.load(f)
    seed1, labels1 = candidates_to_metrics(candidates_good, 0)
  seed2 = []
  labels2 = []
  with open('../files/known_bad.txt', 'r') as f:
    candidates_bad = json.load(f)
    seed2, labels2 = candidates_to_metrics(candidates_bad, 1)
  seed1.extend(seed2)
  labels1.extend(labels2)
  all_users = [[9,25]]
  print(seed1)
  print(labels1)
  probability_calculator = KNNProbabilityCalculator(seed1,
                                                    labels1,
                                                    similarity_fn=similarity_metric)

  ret = []
  for (user, probability) in zip(all_users, probability_calculator.probability(all_users)):
    # update db for user probability
    ret.append({"user":user, "prob":probability})

  return json.dumps(ret)