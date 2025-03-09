# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=dJ7sWiOoK7g

class Solution:
    def jump(self, nums: List[int]) -> int:
        l, r = 0, 0
        res = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1
            r = farthest
            res += 1
        return res