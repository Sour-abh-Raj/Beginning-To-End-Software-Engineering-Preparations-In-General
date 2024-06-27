class Solution:
    def sortColors(self, nums: List[int]) -> None:
        cnt0 = 0
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                cnt1 += 1
            else:
                cnt2 += 1
        for i in range(cnt0):
            nums[i] = 0
        idx_1 = cnt0 + cnt1
        for i in range(cnt0, idx_1):
            nums[i] = 1
        for i in range(idx_1, len(nums)):
            nums[i] = 2