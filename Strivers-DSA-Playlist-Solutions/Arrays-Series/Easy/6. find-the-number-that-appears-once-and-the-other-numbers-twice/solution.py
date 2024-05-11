# Solution using XOR operator
# a ^ a = 0
# a ^ 0 = a
# 0 ^ a = a
# 0 ^ 0 = 0
# ^ is the XOR operator
# Time: O(N)
# Space: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorr = 0
        for num in nums:
            xorr ^= num
        return xorr

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 3, 2, 4, 1, 3, 2]))