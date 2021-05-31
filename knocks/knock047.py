import numpy as np


def exec():
    X = np.arange(8)
    Y = X + 0.5
    C = 1.0 / np.subtract.outer(X, Y)
    print(np.linalg.det(C))
