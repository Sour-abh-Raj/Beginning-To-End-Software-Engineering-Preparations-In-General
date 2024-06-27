class Solution:
    def sortColors(self, nums: list[int]) -> None:
        if len(nums) <= 1:
            return nums
        pivot = nums[len(nums) // 2]
        left = [x for x in nums if x < pivot]
        middle = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]
        return self.sortColors(left) + middle + self.sortColors(right)

nums = [2,0,2,1,1,0]
sol = Solution()
print(sol.sortColors(nums))