import numpy as np


def exec():
    Z = np.zeros(10)
    print("%d bytes" % (Z.size * Z.itemsize))
