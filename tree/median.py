import heapq
from numpy import median


class Median(object):
    def __init__(self):
        self.left = []
        self.right = []

    def add(self, element):
        neg = 0 - element
        # assume left is equal or one longer than right at all times, and maintain this
        if not self.left:
            # first element
            heapq.heappush(self.left, neg)
        elif len(self.left) == len(self.right):
            # they are equal, so we end up putting one on the left
            if element <= abs(self.right[0]):
                heapq.heappush(self.left, neg)
            else:
                heapq.heappush(self.left, 0 - heapq.heappop(self.right))
                heapq.heappush(self.right, element)
        else:
            # this means left is longer than right, so we end up putting one on the right
            if element <= abs(self.left[0]):
                heapq.heappush(self.right, 0 - heapq.heappop(self.left))
                heapq.heappush(self.left, neg)
            else:
                heapq.heappush(self.right, element)

    def current(self):
        return abs(self.left[0])


if __name__ == '__main__':
    # test_list = [6, 1, 3, 4, 9, 2, 10, 11, 5]
    M = Median()
    current_sum = 0
    stat_sum = 0
    stat_list = []
    count = 0
    with open('tree/median.txt', 'r') as file:
        for element in file:
            count += 1
            element = int(element)
            stat_list.append(element)
            stat_list.sort()
            M.add(element)
            stat_mid = stat_list[count // 2] if count % 2 == 1 else stat_list[(count // 2) - 1]
            our_mid = M.current()
            print("element: {}, count {} median: {}, stat: {}".format(element, count, our_mid, stat_mid))
            if our_mid != stat_mid:
                raise Exception
            current_sum += our_mid
            stat_sum += stat_mid
            # current_sum = current_sum % 10000

    print("current sum is now: {}. Stat sum: {}".format(current_sum, stat_sum))
