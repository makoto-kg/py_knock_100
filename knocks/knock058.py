import numpy as np


def exec():
    X = np.random.rand(5, 10)
    print(X)

    Y = X - X.mean(axis=1, keepdims=True)
    print(Y)
