import numpy as np


def exec():
    Z = np.random.randint(0, 10, 50)
    print(np.bincount(Z).argmax())
