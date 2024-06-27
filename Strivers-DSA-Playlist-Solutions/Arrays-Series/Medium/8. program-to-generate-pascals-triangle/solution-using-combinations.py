class Solution:
    def ncr(self, n: int, r: int) -> int:
        if r == 0:
            return 1
        if r > n - r:
            r = n - r
        res = 1
        for i in range(r):
            res *= n - i
            res //= i + 1
        return res
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            res.append([self.ncr(i, j) for j in range(i + 1)])
        return res
    
numRows = 5
sol = Solution()
print(sol.generate(numRows))