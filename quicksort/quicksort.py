import random


def partition(input, pos):
    input[pos], input[0] = input[0], input[pos]
    pivot = input[0]
    i = 1
    for j in range(1, len(input)):
        if input[j] > pivot:
            pass
        else:
            input[i], input[j] = input[j], input[i]
            i += 1
    input[i-1], input[0] = input[0], input[i-1]
    return i-1


def sort(input, iteration=0):
    n = len(input)
    if n < 2:
        return input
    p = random.randint(0, n-1)
    pivot = input[p]
    q = partition(input, p)
    left, right = input[:q], input[q+1:]
    left = sort(left, iteration=iteration+1)
    right = sort(right, iteration=iteration+1)
    return left + [pivot] + right


the_list = [random.randint(0, 1000) for elem in range(10000)]
the_list = sort(the_list)
a_list = the_list.copy()
a_list.sort()
print(the_list == a_list)
