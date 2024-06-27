# Bottom up approach using dfs
# We use edge case that if we are at the bottom row or rightmost column, there is only one way to reach the end from each cell in that row or column
# We start from the bottom right cell and move up and left, adding the number of ways to reach the end from the cell below and to the right of the current cell
# Time complexity: O(m*n)
# Space complexity: O(n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m-1):
            newRow = [1] * n
            for j in range(n-2, -1, -1):
                newRow[j] = newRow[j+1] + row[j]
            row = newRow
        return row[0]