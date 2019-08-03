from sklearn.neighbors import KNeighborsClassifier


class KNNProbabilityCalculator:

  def __init__(self, known_inputs, labels, similarity_fn):
    self.classifier = KNeighborsClassifier(n_neighbors=10, weights='distance', metric=similarity_fn)
    self.classifier.fit(known_inputs, labels)

  def probability(self, sample):
    return self.classifier.predict_proba(sample)[0]
