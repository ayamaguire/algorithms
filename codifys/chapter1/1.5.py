
def increment(string):
    if string.isdigit():
        return str(int(string) + 1)
    assert False


def compress(string):
    result = string[0] + '1'
    for char in string[1:]:
        if result[-2] == char:
            result = result[:-1] + increment(result[-1])
        else:
            result = result + char + '1'
    if len(result) >= len(string):
        return string
    return result


if __name__ == '__main__':
    print(compress('a'))
