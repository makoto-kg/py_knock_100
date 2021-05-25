import numpy as np


def exec():
    Z = np.zeros((8, 8), dtype=int)
    Z[1::2, ::2] = 1
    Z[::2, 1::2] = 1
    print(Z)
