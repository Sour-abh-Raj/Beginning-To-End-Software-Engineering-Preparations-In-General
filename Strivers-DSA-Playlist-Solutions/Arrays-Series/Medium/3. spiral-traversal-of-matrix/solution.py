# Solution using in-place rotation
# In this solution, we first transpose the matrix and then reverse each row.
# Time complexity: O(n^2)
# Space complexity: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(1, n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    print(obj.rotate(matrix))