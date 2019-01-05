import random


running = 0


def partition(input, pos):
    global running
    running = running + len(input) - 1
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


def median_of_three(input):
    n = len(input)
    if n % 2 == 0:
        middle = (n // 2) - 1
    else:
        middle = n // 2
    middle_el = input[middle]
    last_el = input[-1]
    first_el = input[0]
    options = [first_el, middle_el, last_el]
    options.sort()
    if options[1] == first_el:
        return 0
    elif options[1] == middle_el:
        return middle
    else:
        return -1


def sort(input):
    n = len(input)
    if n < 2:
        return input
    # p = random.randint(0, n-1)
    # p = median_of_three(input)
    p = 0
    pivot = input[p]
    q = partition(input, p)
    left, right = input[:q], input[q+1:]
    left = sort(left)
    right = sort(right)
    return left + [pivot] + right


def inplace_partition(input, pos, left, right):
    input[pos+left], input[left] = input[left], input[pos+left]
    # print(input)
    pivot = input[left]
    i = left + 1
    for j in range(left+1, right):
        if input[j] > pivot:
            pass
        else:
            input[i], input[j] = input[j], input[i]
            i += 1
    input[i-1], input[left] = input[left], input[i-1]
    return i-1


def inplace_sort(input, left=None, right=None):
    if left is None or right is None:
        n = len(input)
        left = 0
        right = n
    else:
        n = right - left
    if n < 2:
        return
    p = 0
    q = inplace_partition(input, p, left, right)
    inplace_sort(input, left=left, right=q)
    inplace_sort(input, left=q+1, right=n+left)


if __name__ == '__main__':
    # the_list = [random.randint(0, 10000) for elem in range(100000)]
    # a_list = the_list.copy()
    # inplace_sort(the_list)
    # a_list.sort()
    # print(the_list == a_list)

    with open('quicksort/numbers.txt', 'r') as f:
        integers = [int(line) for line in f]

    sort(integers)
    print(running)
