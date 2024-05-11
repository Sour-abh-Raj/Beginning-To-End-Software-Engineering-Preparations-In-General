class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        sort = [0] * (n+1)
        for i in range(n):
            sort[nums[i]] = nums[i]
        for i in range(n + 1):
            if (sort[i] != i):
                return i
        return n
    
if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(arr))

# def missingNumber(self, nums: List[int]) -> int:
