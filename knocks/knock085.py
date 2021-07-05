import numpy as np


class Symetric(np.ndarray):
    def __setitem__(self, index, value):
        i, j = index
        super(Symetric, self).__setitem__((i, j), value)
        super(Symetric, self).__setitem__((j, i), value)


def symetric(Z):
    return np.asarray(Z + Z.T - np.diag(Z.diagonal())).view(Symetric)


def exec():
    S = symetric(np.random.randint(0, 10, (5, 5)))
    S[2, 3] = 42
    print(S)
