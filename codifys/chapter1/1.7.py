import random


def zero(matrix):
    zeros = []
    for i, line in enumerate(matrix):
        for j, elem in enumerate(line):
            if elem == 0:
                zeros.append((i, j))
    for elem in zeros:
        for i, line in enumerate(matrix):
            if i == elem[0]:
                matrix[i] = [0 for j in range(len(matrix[0]))]
            matrix[i][elem[0]] = 0


if __name__ == '__main__':
    n = 7
    x = [[random.randint(0, 10) for x in range(n)] for y in range(n)]
    for line in x:
        print(line)
    print()
    zero(x)
    for line in x:
        print(line)
