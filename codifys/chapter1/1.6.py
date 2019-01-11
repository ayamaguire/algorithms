import random


def rotate(matrix):
    """ we get to assume it is n by n"""
    n = len(matrix)
    return [[line[n-i-1] for line in matrix] for i in range(len(matrix[0]))]


def inplace_rotate(matrix):
    n = len(matrix)
    m = n // 2 if n % 2 == 0 else n // 2 + 1
    for i in range(m):
        for j in range(n // 2):
            a, b, c, d = matrix[i][j], matrix[j][n-i-1], matrix[n-j-1][i], matrix[n-i-1][n-j-1]
            matrix[i][j], matrix[j][n - i - 1], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1] = b, d, a, c


if __name__ == '__main__':
    n = 1000
    x = [[random.randint(0, n) for x in range(n)] for y in range(n)]
    y = rotate(x)
    inplace_rotate(x)
    print(x == y)
