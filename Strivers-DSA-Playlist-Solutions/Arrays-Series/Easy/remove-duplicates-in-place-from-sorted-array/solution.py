# Solution using two pointers approach
# Time: O(n)
# Space: O(1)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
        for j in range(i + 1, len(nums)):
            nums[j] = '_'
        return (i+1)

if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(arr))
    print(arr)