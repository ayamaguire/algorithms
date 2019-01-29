
def two_sum(target, i, numset):
    j = target - i
    if j in numset:
        return True
    return False


if __name__ == '__main__':
    numbers = set()
    totals = 0
    with open('2sum/numbers.txt', 'r') as file:
        for line in file:
            numbers.add(int(line))

    for t in range(-10000, 10001):
        print("Searching for target {}".format(t))
        for i in numbers:
            if two_sum(t, i, numbers):
                print("    Found pair: {}, {}".format(i, t-i))
                totals += 1
                break

    print("Total: {}".format(totals))
