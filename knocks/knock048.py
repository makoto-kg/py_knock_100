import numpy as np


def exec():
    for dtype in [np.int8, np.int32, np.int64]:
        print(np.iinfo(dtype).min)
        print(np.iinfo(dtype).max)
    for dtype in [np.float32, np.float64, np.float128]:
        print(np.finfo(dtype).min)
        print(np.finfo(dtype).max)
