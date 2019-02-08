from collections import defaultdict, Counter


def sherlock(s):
    total = 0
    for length in range(1, len(s)):
        # length is length of substrings we're currently examining
        n = len(s) - length + 1  # number of substrings per iteration
        substring_counter = defaultdict(int)
        for counter in [Counter(s[j:j+length]) for j in range(n)]:
            subtuples = frozenset({(character, number) for character, number in counter.items()})
            substring_counter[subtuples] += 1

        for key, val in substring_counter.items():
            total += summand(val)

    return total


def summand(n):
    return n * (n-1) // 2 # n choose 2 (number of matching pairs in string repeated n times)


if __name__ == '__main__':
    print(sherlock('abab'))
