import heapq
import random
import time


def solution(A):
    heapq.heapify(A)
    minimum = heapq.heappop(A)
    found = False
    while minimum <= 0:
        try:
            minimum = heapq.heappop(A)
        except IndexError:
            return 1
    if minimum > 1:
        return 1
    next = heapq.heappop(A)
    while not found:
        if next <= minimum + 1:
            minimum = next
            try:
                next = heapq.heappop(A)
            except IndexError:
                return minimum + 1

        else:
            return minimum + 1


def check(A):
    maximum = max(A)
    if maximum <= 0:
        return 1
    for i in range(1, maximum):
        if i in A:
            pass
        else:
            return i
    return maximum + 1


B = [random.randint(-100000, 100000) for i in range(-10000, 10001)]
print(check(B))

now = time.time()
print(solution(B))
print(time.time() - now)
B.sort()
print(B)

