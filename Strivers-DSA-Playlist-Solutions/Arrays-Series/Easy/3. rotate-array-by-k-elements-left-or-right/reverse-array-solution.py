class Solution:
    def Reverse(arr, start, end):
        while (start <= end):
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start += 1
            end -= 1

    def Rotateeletoright(arr, n, k):
        Reverse(arr, 0, n - k - 1)
        Reverse(arr, n - k, n - 1)
        Reverse(arr, 0, n - 1)
        return arr

    def Rotateeletoleft(arr, n, k):
        Reverse(arr, 0, k - 1)
        Reverse(arr, k, n - 1)
        Reverse(arr, 0, n - 1)
        return arr

arr = [1, 2, 3, 4, 5, 6, 7]
n = 7
k = 3
print(Solution.Rotateeletoright(arr, n, k))
print(Solution.Rotateeletoleft(arr, n, k))