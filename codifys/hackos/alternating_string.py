import numpy as np


def make_alternating_np(s):
    a = np.diff(np.array(s))
    idxs = np.nonzero(a)[0]
    idxs = np.append(idxs,idxs[-1]+1)
    print(np.array(s)[idxs])


def make_alternating(s):
    total = 0
    prev = s[0]
    for char in s[1:]:
        if char == prev:
            total += 1
        prev = char
    return total

print(make_alternating([1,0,1, 1, 0, 1,1,1,1]))

# 2 1 5 8 4
[2, 1, 7, 10, 11]
