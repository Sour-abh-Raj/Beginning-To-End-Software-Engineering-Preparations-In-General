def isSorted(arr, n):
    for i in range(n):
        for j in range(i + 1, n):
            if arr[j] < arr[i]:
                return 0

    return 1