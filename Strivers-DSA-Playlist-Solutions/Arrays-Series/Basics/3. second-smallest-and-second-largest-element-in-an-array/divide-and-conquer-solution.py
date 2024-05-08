def getSecondOrderElements(n: int,  arr: [int]) -> [int]:
    a = [0, 0]
    if n == 0 or n == 1:
        return [-1]
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    a[0] = second_large
    a[1] = second_small
    return a