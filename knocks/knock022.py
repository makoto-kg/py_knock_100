import numpy as np


def exec():
    Z = np.random.random((5, 5))
    Z = (Z - np.mean(Z)) / (np.std(Z))
    print(Z)
