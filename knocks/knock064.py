import numpy as np


def exec():
    Z = np.ones(10)
    print(Z)
    data = np.random.randint(0, len(Z), 20)
    Z += np.bincount(data, minlength=len(Z))
    print(Z)
