# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=ycAq8iqh0TI

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        m = len(nums)
        l , r = 0, 0
        if m == 0 or m == 1 or m == 2:
            return m
        while r < m:
            cnt = 1
            while r + 1 < m and nums[r] == nums[r + 1]:
                r += 1
                cnt += 1
            for i in range(min(2, cnt)):
                nums[l] = nums[r]
                l += 1
            r += 1
        return l
            

        