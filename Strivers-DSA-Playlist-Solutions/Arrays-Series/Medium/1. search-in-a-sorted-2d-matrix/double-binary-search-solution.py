# Solution using two binary searches. The first binary search is used to find the row where the target is located. The second binary search is used to find the target in the row found by the first binary search.
# Time complexity: O(log(m) + log(n))
# Space complexity: O(1)
# Runtime: 31 ms

class Solution:
    def binarySearch(self, matrix: List[int], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        if matrix[left] == target or matrix[right] == target:
            return True
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[mid] == target:
                return True
            elif matrix[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n-1]:
                for j in range(n):
                    return self.binarySearch(matrix[i], target)
        return False
    
