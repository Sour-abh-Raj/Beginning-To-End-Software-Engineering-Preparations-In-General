class Solution:
  def searchMatrix(self, matrix, target):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == target:
                return True
    return False
    
if __name__ == "__main__":
  s = Solution()
  matrix = [[1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
  target = 3
  print(s.searchMatrix(matrix, target))