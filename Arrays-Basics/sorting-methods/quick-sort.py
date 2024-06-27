# Dutch National Flag approach

def quickSort1(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quickSort1(left) + middle + quickSort1(right)

arr1 = [3, 6, 8, 10, 1, 2, 1]
print(quickSort1(arr1))

# Divide and conquer approach

def partition(arr: list[int], low: int, high: int) -> int:
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickSort2(arr: list[int], low: int, high: int) -> list[int]:
    if low < high:
        pi = partition(arr, low, high)
        quickSort2(arr, low, pi - 1)
        quickSort2(arr, pi + 1, high)
    return arr

arr2 = [3, 6, 8, 10, 1, 2, 1]
print(quickSort2(arr2, 0, len(arr2) - 1))

# Time complexity: O(n log n) - average case, O(n^2) - worst case
# Space complexity: O(log n) - average case, O(n) - worst case
#