
def reverse(string):
    chars_list = list(string)
    new_str = ''
    for elem in chars_list[::-1]:
        new_str += elem
    return new_str


test_strings = ["abc", "aaa", "34hgabdlqoajdo", "abcdefghijklmnopqrstuvwxyz"]
for string in test_strings:
    print(reverse(string))
