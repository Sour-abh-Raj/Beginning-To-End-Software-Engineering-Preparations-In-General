# Time Complexity: O(N^2)
# Space Complexity: O(N^2)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        rotated = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                rotated[j][n - i - 1] = matrix[i][j]
        return rotated
    
if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    obj = Solution()
    print(obj.rotate(matrix))