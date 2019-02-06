
def count_swaps(arr):
    swaps = 0
    for i in range(len(arr)):
        min = arr[i]
        index = i
        for j in range(i+1, len(arr)):
            if arr[j] < min:
                min = arr[j]
                index = j
        if i != index:
            arr[i], arr[index] = arr[index], arr[i]
            swaps += 1
    return swaps
