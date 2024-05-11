class Solution:
    def shiftArrayToRight(nums, k):
        n = len(nums)
        if not nums:
            return []
        elif k == 0 or k == n or n == 1:
            return nums
        k = k % n
        return nums[-k:] + nums[:-k]

    def shiftArrayToLeft(nums, k):
        n = len(nums)
        if not nums:
            return []
        elif k == 0 or k == n or n == 1:
            return nums
        k = k % n
        return nums[k:] + nums[:k]

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 2
    print(Solution.shiftArrayToRight(nums, k))
    print(Solution.shiftArrayToLeft(nums, k))