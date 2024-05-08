# This solution uses a brute force approach to solve the problem.
# It uses an extra array to store the rotated array.
# This solution is not optimal as it uses extra space.
# The time complexity of this solution is O(n) and the space complexity is O(n).

def solve(arr, n):
    temp = [0] * n
    for i in range(1, n):
        temp[i - 1] = arr[i]
    temp[n - 1] = arr[0]
    for i in range(n):
        arr[i] = temp[i]
    return arr