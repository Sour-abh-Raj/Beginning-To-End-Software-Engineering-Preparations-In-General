class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        summation = (n * (n + 1)) // 2
        s2 = sum(nums)
        missingNum = summation - s2
        return missingNum
    
if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(arr))