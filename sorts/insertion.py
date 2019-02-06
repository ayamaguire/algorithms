
def insertion_sort(arr):
    """ Take in an unsorted array and return a sorted array. We use binary search."""
    sorted = arr[:1]
    for elem in arr[1:]:
        i = binary_search(sorted, elem)
        sorted.insert(i, elem)
    return sorted


def binary_search(arr, x):
    """ Assume array is sorted, find place for x."""
    n = len(arr)
    if n == 1:
        if arr[0] > x:
            return 0
        else:
            return 1
    if not n:
        # I don't think we ever hit this
        return 0
    if arr[n // 2] > x:
        return binary_search(arr[:n//2], x)
    else:
        return binary_search(arr[n//2:], x) + n // 2


if __name__ == '__main__':
    test_array = [0, 5, 1, 2, 4, 3]
    print(insertion_sort(test_array))
