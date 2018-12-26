import random


def karatsuba(in1, in2):
    """ Take in two strings so that nothing is lost"""
    # make x the larger number, always
    if int(in1) > int(in2):
        x, y = in1, in2
    else:
        y, x = in1, in2

    n, m = len(x), len(y)
    if n == 1 or m == 1:
        return str(int(x) * int(y))
    p = m // 2
    a, b = x[:-p], x[-p:]
    c, d = y[:-p], y[-p:]
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    aplusb = str(int(a) + int(b))
    cplusd = str(int(c) + int(d))
    mid = karatsuba(aplusb, cplusd)
    bcplusad = str(int(mid) - int(ac) - int(bd))

    final_sum = str(int(ac + '0' * (2*p)) + int(bcplusad + '0' * p) + int(bd))
    return final_sum


# num1, num2 = random.randint(100000000000, 1000000000000), random.randint(10000000000, 100000000000)
# product = num1*num2
# karaproduct = karatsuba(str(num1), str(num2))
# print(num1, num2, product, karaproduct, str(product) == karaproduct)

print(karatsuba('3141592653589793238462643383279502884197169399375105820974944592', '2718281828459045235360287471352662497757247093699959574966967627'))
