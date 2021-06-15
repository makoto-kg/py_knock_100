import numpy as np


def exec():
    X = [1, 2, 3, 4, 5, 6]
    data = [1, 3, 9, 3, 4, 1]
    F = np.bincount(data, X)
    print(F)
