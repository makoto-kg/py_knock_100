import numpy as np


def exec():
    X, Y = np.meshgrid(np.linspace(-1, 1, 10), np.linspace(-1, 1, 10))
    print(X)
    print(Y)
    D = np.sqrt(X*X + Y*Y)
    sigma, mu = 1.0, 0.0
    G = np.exp(-((D-mu)**2 / (2.0 * sigma**2)))
    print(G)
