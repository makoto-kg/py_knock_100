import numpy as np


def exec():
    Z = np.random.random(10)
    print(Z)
    print(Z.argmax())
    Z[Z.argmax()] = 0
    print(Z)
