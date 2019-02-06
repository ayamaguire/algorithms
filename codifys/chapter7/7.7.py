# find the kth smallest number whose factors are only 3, 5, 7

import heapq


def next_357():
    factors = [3, 5 , 7]
    heap = [3, 5, 7]
    seen = {3, 5, 7}
    while heap:
        rv = heapq.heappop(heap)
        for factor in factors:
            if rv * factor not in seen:
                heapq.heappush(heap, rv * factor)
                seen.add(rv * factor)
        yield rv


if __name__ == '__main__':
    a = next_357()
    print(next(a))
