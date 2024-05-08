def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return 0
    return 1