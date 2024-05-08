def getSecondOrderElements(n: int,  arr: [int]) -> [int]:
    a = [0, 0]
    if n == 0 or n == 1:
        print(-1, -1)
    arr.sort()
    small = arr[1]
    large = arr[n-2]
    a[0] = large
    a[1] = small
    return a