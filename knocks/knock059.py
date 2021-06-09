import numpy as np


def exec():
    Z = np.random.randint(0, 10, (3, 3))
    print(Z)
    print(Z[Z[:, 1].argsort()])
