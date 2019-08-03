from numpy.linalg import norm


def similarity_metric(first, second):
  return norm(first - second)
