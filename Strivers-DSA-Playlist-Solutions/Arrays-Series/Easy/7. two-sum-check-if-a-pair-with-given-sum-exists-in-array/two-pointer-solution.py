# Solution using Two Pointer Technique (Sorting)
# Time Complexity: O(nlogn) + O(n) = O(nlogn) due to sortingss
# Space Complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        i, j = 0, len(nums) - 1
        while i < j:
            if (nums[i] + nums[j] == target):
                return [i, j]
            elif (nums[i] + nums[j] < target):
                i += 1
            else:
                j -= 1
        return []

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))