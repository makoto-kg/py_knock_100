import numpy as np


def exec():
    A = np.random.randint(0, 2, 5)
    B = np.random.randint(0, 2, 5)
    print(np.allclose(A, B))
