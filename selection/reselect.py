import random


def inplace_partition(inlist, pos, beginning=None, end=None):
    n = len(inlist)
    beginning = beginning or 0
    end = end or n
    inlist[pos], inlist[beginning] = inlist[beginning], inlist[pos]
    # print(inlist)
    pivot = inlist[beginning]
    i = beginning + 1
    for j in range(beginning + 1, end):
        if inlist[j] > pivot:
            pass
        else:
            inlist[i], inlist[j] = inlist[j], inlist[i]
            i += 1
    inlist[i - 1], inlist[beginning] = inlist[beginning], inlist[i - 1]
    return i-1


def select(inlist, order, beginning=None, end=None):
    n = len(inlist)
    beginning = beginning or 0
    end = end or n
    n = end - beginning
    # print("running select with beginning {} and end {} so list is {}".format(beginning, end, inlist[beginning:end]))
    if n == 1:
        return beginning
    # pivot = random.randint(0, n-1)
    pivot = beginning
    # print("calling partition on pivot {}, {}".format(pivot, inlist[pivot]))
    j = inplace_partition(inlist, pivot, beginning, end)
    # print("j is {}, order is {} and list now {}".format(j, order, inlist))
    if order < j:
        return select(inlist, order, beginning, j)
    elif order > j:
        return select(inlist, order, j+1, end)
    else:
        return j


if __name__ == '__main__':
    the_list = [3, 4, 1, 8, 2, 5, 9, 7, 6, 0]
    print(the_list)
    k = select(the_list, 4)
    print(k, the_list)
    print("found k in the {}th place and it's {}".format(k, the_list[k]))

