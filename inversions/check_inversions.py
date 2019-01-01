from inversions import divide_and_conquer, brute_force
import time

with open('inversions/integers.txt', 'r') as f:
    integers = [int(line) for line in f]


if __name__ == '__main__':
    # 2407905288
    now = time.time()
    print(brute_force.count_inversions(integers))
    print(time.time() - now)
