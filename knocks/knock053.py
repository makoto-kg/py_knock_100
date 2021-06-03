import numpy as np


def exec():
    Z = (np.random.rand(10)*100).astype(np.float32)
    print(Z)
    Y = Z.view(np.int32)
    print(Y)
    Y[:] = Z
    print(Y)
