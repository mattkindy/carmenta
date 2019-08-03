from flask import Blueprint

from api.api import api_root
from clustering.knn_probability import KNNProbabilityCalculator
from clustering.similarity import similarity_metric

scrape_root = Blueprint('cluster', __name__, url_prefix="{}/cluster".format(api_root.url_prefix))


@scrape_root.route('/', methods=['POST'])
def recalculate_clustering():
  # get user resource
  seed_users = []
  all_users = []
  probability_calculator = KNNProbabilityCalculator([u.x for u in seed_users],
                                                    [u.y for u in seed_users],
                                                    similarity_fn=similarity_metric)

  for (user, probability) in zip(all_users, probability_calculator.probability(all_users)):
    # update db for user probability
    pass
