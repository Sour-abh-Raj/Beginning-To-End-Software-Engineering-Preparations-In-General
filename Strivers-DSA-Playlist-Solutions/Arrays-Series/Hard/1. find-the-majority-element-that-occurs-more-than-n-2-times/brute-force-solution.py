class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
                if cnt[num] > len(nums) // 2:
                    return num
            else:
                cnt[num] = 1
        return -1
    
nums = [3, 3, 4, 2, 4, 4, 2, 4, 4]
sol = Solution()
print(sol.majorityElement(nums))