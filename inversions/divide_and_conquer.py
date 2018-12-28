from inversions import brute_force
import random


def count_merge_inversions(inlist):
    n = len(inlist)
    if n == 1:
        return inlist, 0
    else:
        a, left = count_merge_inversions(inlist[:n // 2])
        b, right = count_merge_inversions(inlist[n // 2:])
        the_list, splits = merge(a, b)
        return the_list, left + right + splits


def merge(x, y):
    is_merged = False
    i, j = 0, 0
    inversions = 0
    output = []
    while is_merged is False:
        if x[i] <= y[j]:
            output.append(x[i])
            i += 1
        else:
            # [1, 4, 5] [2, 3, 4]
            output.append(y[j])
            inversions += len(x[i:])
            j += 1
        if i == len(x):
            for elem in range(j, len(y)):
                output.append(y[elem])
            is_merged = True
        if j == len(y):
            for elem in range(i, len(x)):
                output.append(x[elem])
            is_merged = True
    return output, inversions


num = 10000
test = [random.randint(1, num) for x in range(num)]
brute = brute_force.count_inversions(test)
divconq = count_merge_inversions(test)[1]
print(brute, divconq, brute == divconq)
