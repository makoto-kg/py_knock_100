import numpy as np


def exec():
    Z = np.arange(100)
    v = np.random.uniform(0, 100)
    index = (np.abs(Z-v)).argmin()
    print(Z)
    print(Z[index])
