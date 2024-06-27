class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            res = [[1], [1, 1]]
        for i in range(2, numRows):
            el = [1]
            for j in range(1, i):
                el.append(res[i-1][j] + res[i-1][j-1])
            el.append(1)
            res.append(el)
        return res

        
numRows = 5
sol = Solution()
print(sol.generate(numRows))