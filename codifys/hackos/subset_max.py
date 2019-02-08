import heapq


def subset_max(arr):
    maxes = [0, arr[0] * -1]
    heapq.heapify(maxes)
    last = arr[1]
    # print("begin with {} with last {}".format(maxes, last))
    for elem in arr[2:]:
        current = elem + (maxes[0] * -1)
        heapq.heappush(maxes, last * -1)
        last = current
        # print("elem: {}, last: {}. maxes: {}".format(elem, last, maxes))
    heapq.heappush(maxes, last * -1)
    # print(maxes)
    return heapq.heappop(maxes) * -1


if __name__ == '__main__':
    with open('/Users/ayamaguire/PycharmProjects/algorithms/algorithms/codifys/hackos/input00.txt', 'r') as f:
        for line in f:
            els = list(map(int, line.rstrip().split()))

a = [-2, 1, 3, -4, 5]
# max_heap = [0, -2, 1, 3, -3, 8]
# current = 8
# last = 8
print(subset_max(els))
