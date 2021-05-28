import numpy as np


def generate():
    for x in range(10):
        yield x


def exec():
    Z = np.fromiter(generate(), dtype=float, count=-1)
    print(Z)
