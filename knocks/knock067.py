import numpy as np


def exec():
    A = np.random.randint(0, 10, (3, 4, 3, 4))
    sum = A.sum(axis=(-2, -1))
    print(sum)
