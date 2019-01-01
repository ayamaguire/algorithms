

def closest_pair(inlist):
    """ takes in a list of points (x, y) and determines which two are closest (euclidian)
    :param inlist: list of tuples representing x and y vals
    """
    n = len(inlist)
    if n == 1:
        return inlist, (float('inf'), float('inf')), float('inf')
    minimum = float('inf')
    pair = None
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(inlist[i], inlist[j])
            if dist < minimum:
                minimum = dist
                pair = i, j
    return inlist[pair[0]], inlist[pair[1]], minimum


def distance(a, b):
    if a == float('inf') or b == float('inf'):
        return float('inf')
    x, y = b[0] - a[0], b[1] - a[1]
    return (x ** 2 + y ** 2) ** 0.5


if __name__ == '__main__':
    pass
