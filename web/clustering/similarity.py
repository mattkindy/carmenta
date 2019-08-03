from numpy.linalg import norm
import json
from clustering.metrics import *
from scraper.interface.candidate import Candidate

# Metrics are Job Title, Current Company (Ranked), Past Companies (Averaged)
metrics = []

def similarity_metric(first, second):
    return norm(first - second)



#Takes candidate json object and converts the values to appropriate input for similarity matrix
def candidates_to_metrics(candidates):
    X = []
    for candidate in candidates:
        x = [len(candidate["name"])]
        college_len = 0
        if candidate["college"] != None:
            college_len = len(candidate["college"])
        x.append(college_len)
        X.append(x)

    return X
