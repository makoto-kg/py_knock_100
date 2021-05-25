import numpy as np


def exec():
    Z = np.random.uniform(-10, +10, 10)
    print(np.copysign(np.ceil(np.abs(Z)), Z))
