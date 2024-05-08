class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_one = 0
        for num in nums:
            if num == 1:
                count += 1
                max_one = max(max_one, count)
            else:
                count = 0
        return max_one
