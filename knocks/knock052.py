import numpy as np


def exec():
    Z = np.random.random((10, 2))
    X, Y = np.atleast_2d(Z[:, 0], Z[:, 1])
    D = np.sqrt((X - X.T)**2 + (Y - Y.T)**2)
    print(D)
