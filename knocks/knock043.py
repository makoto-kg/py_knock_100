import numpy as np


def exec():
    Z = np.zeros(10)
    Z.flags.writeable = False

    try:
        Z[0] = 1
    except Exception as e:
        print(e)
