import numpy as np


def exec():
    Z = np.diag(1 + np.arange(4), k=-1)
    print(Z)
