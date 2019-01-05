import math


def solution(N):
    # write your code in Python 3.6
    pass


def convert_to_binary(N):
    """ returns a list representation of the binary number N"""
    if N == 0:
        return [0]
    if N == 1:
        return [1]
    if N == 2:
        return [1, 0]
    n = math.floor(math.log(N, 2))
    bin = [0 for i in range(n+1)]
    bin[0] = 1
    print("bin is {}".format(bin))
    rem = N - 2 ** n
    print("rem is {}".format(rem))
    bin_rem = convert_to_binary(rem)
    for i in range(-1, (len(bin_rem) * - 1) - 1, -1):
        bin[i] = bin_rem[i]
    return bin


print(convert_to_binary(2147483646))
