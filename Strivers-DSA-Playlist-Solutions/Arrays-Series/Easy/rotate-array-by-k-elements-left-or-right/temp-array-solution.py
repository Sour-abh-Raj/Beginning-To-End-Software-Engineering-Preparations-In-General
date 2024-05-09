class Solution:
    def rotate_to_right(arr, n, k):
        if n == 0:
            return
        k = k % n
        if k > n:
            return
        temp = arr[n - k:]
        for i in range(n - k - 1, -1, -1):
            arr[i + k] = arr[i]
        for i in range(k):
            arr[i] = temp[i]
        return arr

    def rotate_to_left(arr, n, k):
        if n == 0:
            return
        k = k % n
        if k > n:
            return
        temp = arr[:k]
        for i in range(n - k):
            arr[i] = arr[i + k]
        for i in range(n - k, n):
            arr[i] = temp[i - n + k]
        return arr

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    n = 7
    print(Solution.rotate_to_right(nums, n, k))
    print(Solution.rotate_to_left(nums, n, k))