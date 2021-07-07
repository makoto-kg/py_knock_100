import numpy as np


def exec():
    p, n = 10, 20
    M = np.ones((p, n, n))
    V = np.ones((p, n, 1))
    S = np.tensordot(M, V, axes=[[0, 2], [0, 1]])
    print(S)
