import numpy as np
from numpy.lib import stride_tricks


def rolling(a, window):
    shape = (a.size - window + 1, window)
    strides = (a.strides[0], a.strides[0])
    return stride_tricks.as_strided(a, shape=shape, strides=strides)


def exec():
    Z = rolling(np.arange(10), 3)
    print(Z)
