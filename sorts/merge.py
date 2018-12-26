import time
import random
from matplotlib import pyplot as plt


def merge_sort(inlist):
    n = len(inlist)
    if n == 1:
        return inlist
    else:
        a, b = merge_sort(inlist[:n // 2]), merge_sort(inlist[n // 2:])
        return merged(a, b)


def merged(x, y):
    is_merged = False
    i, j = 0, 0
    output = []
    while is_merged is False:
        if x[i] <= y[j]:
            output.append(x[i])
            i += 1
        else:
            output.append(y[j])
            j += 1
        if i == len(x):
            for elem in range(j, len(y)):
                output.append(y[elem])
            is_merged = True
        if j == len(y):
            for elem in range(i, len(x)):
                output.append(x[elem])
            is_merged = True
    return output
