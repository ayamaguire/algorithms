
def is_anagram(str1, str2):
    chars1 = dict()
    chars2 = dict()
    for char in str1:
        if chars1.get(char):
            chars1[char] += 1
        else:
            chars1[char] = 1
    for char in str2:
        if chars2.get(char):
            chars2[char] += 1
        else:
            chars2[char] = 1
    return chars1 == chars2


def is_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    for i, char in enumerate(list(str1)):
        if str1[i:] + str1[:i] == str2:
            return True
    return False


if __name__ == "__main__":
    print(is_permutation("bcdefga", "abcdefg"))
