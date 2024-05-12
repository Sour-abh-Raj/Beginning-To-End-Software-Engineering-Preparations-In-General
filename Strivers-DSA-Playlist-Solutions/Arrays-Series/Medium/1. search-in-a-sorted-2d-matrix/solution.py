# Solution using binary search considering the 2D matrix as a 1D array.
# Time complexity: O(log(m*n)) = O(log(m) + log(n))
# Space complexity: O(1)
# This solution is better than the previous one because it uses only one binary search instead of two.
# It's flattening the 2D matrix into a 1D array and then applying binary search on it.
# It's also more efficient because it avoids the overhead of calling the binarySearch function for each row.
# Runtime: 39 ms

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = left + (right - left) // 2 # I used this instead of (left + right) // 2 to avoid overflow when left and right are large numbers (e.g. 10^9) and their sum exceeds the maximum value of an integer (2^31 - 1)
            mid_value = matrix[mid // n][mid % n] # mid // n gives the row index and mid % n gives the column index
            
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False