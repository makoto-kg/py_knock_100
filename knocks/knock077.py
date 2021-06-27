import numpy as np


def exec():
    Z = np.random.randint(0, 2, 100)
    print(Z)
    print(np.logical_not(Z, out=Z))

    Z = np.random.uniform(-1.0, 1.0, 100)
    print(Z)
    print(np.negative(Z, out=Z))
