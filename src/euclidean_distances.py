import numpy as np


def euclidean_distances(X, Y):
    """
    Compute the euclidean distance

    Parameters
    ----------
    X: ndarray

    Y: ndarray

    Returns
    -------
    distances: float
    """
    assert (X.shape == Y.shape)
    d = ((X - Y) ** 2).sum()
    return np.sqrt(d)
