# This brute force approach uses a loop which is not necessary.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        for _ in range(k):
            nums.insert(0, nums.pop())