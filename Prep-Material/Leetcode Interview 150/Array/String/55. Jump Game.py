# https://leetcode.com/problems/jump-game/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=Yan0cv2cLy8

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        goal = n - 1
        for i in range(n - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return True if goal == 0 else False