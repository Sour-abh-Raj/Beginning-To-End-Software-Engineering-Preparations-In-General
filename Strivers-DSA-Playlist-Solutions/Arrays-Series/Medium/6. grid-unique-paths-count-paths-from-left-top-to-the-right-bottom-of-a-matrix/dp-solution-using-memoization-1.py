# Top-Down Approach using Memoization

class Solution:
    def countPaths(self, i: int, j: int, m: int, n: int, dp: List[List[int]]) -> int:
        if i == m - 1 and j == n - 1:
            return 1
        if i >= m or j >= n:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        dp[i][j] = self.countPaths(i+1, j, m, n, dp) + self.countPaths(i, j+1, m, n, dp)
        return dp[i][j]
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        i , j = 0, 0
        return self.countPaths(i, j , m, n, dp)