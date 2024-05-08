# This solution is the optimal solution for this problem.
# The time complexity of this solution is O(n) and the space complexity is O(1).

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]