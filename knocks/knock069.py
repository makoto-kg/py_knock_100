import numpy as np


def exec():
    A = np.random.uniform(0, 1, (5, 5))
    B = np.random.uniform(0, 1, (5, 5))

    R = np.diag(np.dot(A, B))
    print(R)
