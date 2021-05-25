import numpy as np


def exec():
    Z = np.arange(11)
    Z[(3 < Z) & (Z < 8)] *= -1
    print(Z)
