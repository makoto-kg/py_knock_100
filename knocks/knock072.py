import numpy as np


def exec():
    A = np.arange(25).reshape(5, 5)
    print(A)
    A[[0, 1]] = A[[1, 0]]
    print(A)
