from collections import defaultdict

def sherlock(s):
    # s = abcd
    # sets = [{a: 1}, {b: 1}, {c: 1}, {d: 1}]
    # sets = [{a: 1, b: 1}, {b, c}, {c, d}]
    # sets = [{a, b, c}, {b, c, d}]
    total = 0
    for i in range(1, len(s)):
        # i is length of substrings
        n = len(s) - i + 1  # number of substrings per set
        substrings = []
        for j in range(n):
            substringdict = defaultdict(int)
            for char in s[j:j+i]:
                substringdict[char] += 1
            substrings.append(substringdict)
        unique_substrings = []
        for substring in substrings:
            if substring in unique_substrings:
                pass
            else:
                unique_substrings.append(substring)
        print(substrings)
        print(unique_substrings)
        subtotal = len(substrings) - len(unique_substrings)
        total += subtotal
    return total


if __name__ == '__main__':
    print(sherlock('abab'))
