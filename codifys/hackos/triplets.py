from collections import defaultdict

# [1, 1, 3, 1, 3, 9, 9, 17, 27] -> 2 + 2 + 2 + 2 = 8


def candidates(r=2, max=10 ** 9):
    n = 1
    result = 1
    while result < max:
        yield result
        result = r ** n
        n += 1


def count_triplets_in_array(arr, r):
    total = 0
    indices = defaultdict(list)
    for i, elem in enumerate(arr):
        indices[elem].append(i)
    if r == 1:
        return counter(indices)
    number = 1
    while number * r * r < 10 ** 9:
        locations = indices[number], indices[number * r], indices[number * r * r]
        # print("Numbers {} at Locations {} found {}".format((number, number * r, number * r * r), locations, helper(locations)))
        total += helper(locations)
        number = number * r
    return total


def counter(indices):
    total = 0
    # we have 1s at [0, 1, 2, 3] ->
    for key, val in indices.items():
        n = len(val)
        total += n * (n - 1) * (n - 2) // (3 * 2)
    return total


def helper(locations):
    # given for example
    # [0, 2], [3, 4], [1, 5] return 4: (0, 3, 5), (0, 4, 5), (2, 3, 5), (2, 4, 5)
    total = 0
    if not all(locations):
        return total
    for high in locations[2]:
        for mid in locations[1]:
            if mid > high:
                break
            for low in locations[0]:
                if low < mid:
                    total += 1
    return total


def count_triplets_badly(arr, r):
    indices = defaultdict(list)
    potentials = defaultdict(list)
    total = 0
    for i, element in enumerate(arr):
        indices[element].append(i)
        if is_geometric(element, r):
            child = element // r
            grandchild = child // r
            for index in indices[child]:
                potentials[(child, index)].append((element, i))
            for index in indices[grandchild]:
                total += len(potentials[(grandchild, index)])
    if r == 1:
        return counter(indices)
    return total


def is_geometric(number, r):
    if r == 1:
        return False
    child = number // r
    grandchild = child // r
    if r * child == number and r * r * grandchild == number:
        return True
    return False


def count_triplets(arr, r):
    total = 0
    squares = {}
    cubes = {}
    for elem in arr:
        if elem in cubes:
            # this means we've seen elem / r and elem / r2, this many times, prior to now
            total += cubes[elem]

        if elem in squares:
            # this means we've seen elem / r, so if we ever see elem * r we better be ready for it
            if elem * r in cubes:
                cubes[elem * r] += squares[elem]
            else:
                cubes[elem * r] = 1

        # now track that we saw this element
        if elem * r in squares:
            squares[elem * r] += 1
        else:
            squares[elem * r] = 1
    return total


def someone_else_did_this(arr, r):
    count = 0
    d2 = {}
    d3 = {}

    for elem in arr:
        if elem in d3:
            count += d3[elem]

        if elem in d2:
            if elem * r in d3:
                d3[elem * r] += d2[elem]
            else :
                d3[elem * r] = d2[elem]

        if elem * r in d2:
            d2[elem * r] += 1
        else:
            d2[elem * r] = 1

    return count

with open('/Users/ayamaguire/PycharmProjects/algorithms/algorithms/codifys/hackos/input06.txt', 'r') as f:
    for line in f:
        els = list(map(int, line.rstrip().split()))

#print(els, len(els))

print(count_triplets(els, 3))
# {1: [0, 2], 3: [3, 4], 9: [1, 5], 27: [6], 81: [7]}
