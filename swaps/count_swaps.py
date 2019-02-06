
def count_swaps(arr):
    sorted = arr[::]
    sorted.sort()
    sorting_dict = {}
    for i, elem in enumerate(sorted):
        sorting_dict[elem] = i

    # now use the sorting_dict dictionary to count swaps
    swaps = 0
    i = 0
    while i < len(arr):
        correct = sorting_dict[arr[i]]
        if i == correct:
            i += 1
        else:
            arr[i], arr[correct] = arr[correct], arr[i]
            swaps += 1
    assert arr == sorted
    return swaps


if __name__ == '__main__':
    array = [4, 3, 1, 2]
    print(count_swaps(array))
