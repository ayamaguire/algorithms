
# determine if a string has all unique characters

# with a dict
def unique_dict(string):
    chars = dict()
    for elem in string:
        if not chars.get(elem):
            chars[elem] = 1
        else:
            return False
    return True


# without a dict (boo)
def unique(string):
    chars_list = list(string)
    chars_set = set(chars_list)
    return len(chars_list) == len(chars_set)


test_strings = ["abc", "aaa", "34hgabdlqoajdo", "abcdefghijklmnopqrstuvw"]
for string in test_strings:
    print(unique(string))
