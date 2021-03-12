import numpy as np
from numpy import random


def getRandomArray(length):
    array = random.permutation(np.arange(1, length + 1, 1))
    return array


def getDecreasingArray(length):
    array = []
    i = length
    while i > 0:
        array.append(i)
        i -= 1
    return array


def readArray():
    pass


def loadArray():
    pass
