# Runtime: 35 ms
# Works in O(n²) time

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.append(nums.pop(i))
            else:
                i += 1
        return nums
