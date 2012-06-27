import numpy as np


def euclidean_distances(X, Y):
    """
    Compute the euclidean distance
    """
    # X and Y should be of same shape
    d = ((X - Y) ** 2).sum()
    return np.sqrt(d)
