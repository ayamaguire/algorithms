from collections import defaultdict


def arrayManipulation(n, queries):
    totals = defaultdict(int)
    for query in queries:
        for i in range(query[0], query[1]+1):
            totals[i] += query[2]
        print(query)
    maximum = 0
    for key, val in totals.items():
        if totals[key] > maximum:
            maximum = val
    return maximum


if __name__ == '__main__':
    n = 10000000
    queries = []
    with open('/Users/ayamaguire/PycharmProjects/algorithms/algorithms/codifys/hackos/input13.txt', 'r') as f:
        for line in f:
            queries.append(list(map(int, line.rstrip().split())))

    result = arrayManipulation(n, queries)
    print(result)
