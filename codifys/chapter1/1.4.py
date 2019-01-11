
def space_replace(string):
    result = string.split(' ')
    return '%20'.join(result)


if __name__ == '__main__':
    print(space_replace('a	a'))
    print(space_replace('b b'))
    print(space_replace('a\na'))
