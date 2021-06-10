import numpy as np


def exec():
    Z = np.random.randint(0, 3, (3, 10))
    print((~Z.any(axis=0)).any())
