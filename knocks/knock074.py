import numpy as np


def exec():
    C = np.bincount([1, 1, 2, 3, 4, 4, 6])
    A = np.repeat(np.arange(len(C)), C)
    print(A)
