import numpy as np


def exec():
    Z1 = np.random.randint(0, 10, 10)
    Z2 = np.random.randint(0, 10, 10)
    print(np.intersect1d(Z1, Z2))
