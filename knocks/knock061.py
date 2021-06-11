import numpy as np


def exec():
    Z = np.random.uniform(0, 1, 10)
    z = 0.5
    m = Z.flat[np.abs(Z-z).argmin()]
    print(Z)
    print(m)
