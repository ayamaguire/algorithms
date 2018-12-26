import time
import random
from matplotlib import pyplot as plt
import numpy


def time_that_shit(func, num=12, avg=10):
    rub_times = []
    test_lengths = [2**n for n in range(1, num)]
    for item in test_lengths:
        average_times = 0
        for i in range(1, avg):
            the_list = [random.randint(1, 10000) for x in range(item)]
            start = time.time()
            func(the_list)
            run_time = time.time() - start
            print(item, run_time)
            average_times += run_time
        average_times = average_times / avg
        rub_times.append(average_times)

    plt.plot(test_lengths, rub_times)
    plt.xlabel("Test lengths")
    plt.ylabel("Rub times")
    plt.show()


if '__name_' == '__main__':
    bab = numpy.linspace(1, 100)
    bablogbab = numpy.log(bab) * bab

    plt.plot(bab, bab)
    plt.plot(bab, bab*bab)
    plt.plot(bab, bablogbab)
    plt.show()
