
def is_substring(s1, s2):
    return s1 in s2


def is_permutation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1, s2 + s2)


if __name__ == '__main__':
    s1, s2 = 'abcdefab', 'cdefab'
    print(is_permutation(s1, s2))
