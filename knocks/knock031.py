import numpy as np


def exec():
    # Z = np.ones(1) / 0

    # Suicide mode on
    defaults = np.seterr(all="ignore")
    Z = np.ones(1) / 0
    print(Z)

    # Back to sanity
    _ = np.seterr(**defaults)

    # Equivalently with acontext manager
    with np.errstate(all="ignore"):
        np.arange(3) / 0
