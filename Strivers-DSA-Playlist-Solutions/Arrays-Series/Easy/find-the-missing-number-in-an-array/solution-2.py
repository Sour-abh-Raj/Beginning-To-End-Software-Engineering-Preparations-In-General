class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xor1 = 0
        xor2 = 0
        for i in range(1, n+1):
            xor1 ^= i
            xor2 ^= nums[i-1]
        return xor1 ^ xor2

    
if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(arr))