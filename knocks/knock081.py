import numpy as np
from numpy.lib import stride_tricks


def exec():
    Z = np.arange(1, 15, dtype=np.uint32)
    R = stride_tricks.as_strided(Z, (11, 4), (4, 4))
    print(R)
