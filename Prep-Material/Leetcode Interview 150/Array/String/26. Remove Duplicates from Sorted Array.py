# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=DEJAZBq0FDA

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0 or l == 1:
            return l
        k = 1
        for i in range(1, l):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k