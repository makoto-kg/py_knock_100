import numpy as np


def exec():
    yesterday = np.datetime64('today') - np.timedelta64(1)
    today = np.datetime64('today')
    tomorrow = np.datetime64('today') + np.timedelta64(1)

    print(yesterday)
    print(today)
    print(tomorrow)
