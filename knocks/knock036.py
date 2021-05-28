import numpy as np


def exec():
    Z = np.random.uniform(0, 10, 10)
    print(Z)
    print(Z - Z % 1)
    print(Z // 1)
    print(np.floor(Z))
    print(Z.astype(int))
    print(np.trunc(Z))
