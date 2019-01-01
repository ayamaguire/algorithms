from closest_points_search import brute_force
import random
import math


def merge_sort_adapted(inlist, coord):
    n = len(inlist)
    if n == 1:
        return inlist
    else:
        a, b = merge_sort_adapted(inlist[:n // 2], coord), merge_sort_adapted(inlist[n // 2:], coord)
        return merge_adapted(a, b, coord)


def merge_adapted(x, y, coord):
    is_merged = False
    i, j = 0, 0
    output = []
    while is_merged is False:
        if x[i][coord] <= y[j][coord]:
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


def closest_pair(inlist):
    n = len(inlist)
    # if n == 1:
    #     return inlist[0], (float('inf'), float('inf')), float('inf')
    # if n == 2:
    #     return inlist[0], inlist[1], brute_force.distance(inlist[0], inlist[1])
    if n < 3:
        p, q, delta = brute_force.closest_pair(inlist)
        return p, q, delta
    sx = merge_sort_adapted(inlist, 0)
    sy = merge_sort_adapted(inlist, 1)
    L, R = sx[:n // 2], sx[n // 2:]
    p1, q1, d1 = closest_pair(L)
    p2, q2, d2 = closest_pair(R)
    # d1, d2 = brute_force.distance(p1, q1), brute_force.distance(p2, q2)
    if d1 < d2:
        delta = d1
        p, q = p1, q1
    else:
        delta = d2
        p, q = p2, q2
    p3, q3, d3 = closest_split_pair(sx, sx, sy, delta)
    if p3 is not None:
        p, q = p3, q3
        delta = d3
    return p, q, delta


def closest_split_pair(inlist, Sx, Sy, Delta):
    # print("entered split pair search with {} and delta {}".format(inlist, Delta))
    n = len(inlist)
    xbar = Sx[:n // 2][-1][0]
    # print("xbar {}".format(xbar))
    sy = filter_list(Sy, xbar - Delta, xbar + Delta)
    # print("After filter: {}".format(sy))
    delta = Delta
    p3, q3 = None, None
    for i in range(len(sy)):
        for j in range(i+1, min(len(sy), 7)):
            # print("looking at {}".format((sy[i], sy[j])))
            d = brute_force.distance(sy[i], sy[j])
            if d < delta:
                p3, q3 = sy[i], sy[j]
                delta = d
                # print("Found a distance {} less than delta".format(d))
    return p3, q3, delta


def filter_list(inlist, minimum, maximum):
    """ We get to assume inlist is sorted by y coordinate and is a list of (a, b) points."""
    outlist = inlist.copy()
    for i, elem in reversed(list(enumerate(outlist))):
        if elem[0] < minimum or elem[0] > maximum:
            outlist.pop(i)
    return outlist


if __name__ == '__main__':
    n, k = 128, 10000
    the_list = [(random.randint(1, k), random.randint(1, k)) for i in range(n)]
    print(the_list)
    print(brute_force.closest_pair(the_list))
    print(closest_pair(the_list))
