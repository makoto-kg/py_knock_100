import numpy as np


def exec():
    Z = np.ones((5, 5))
    Z = np.pad(Z, pad_width=1, mode='constant', constant_values=0)
    print(Z)
