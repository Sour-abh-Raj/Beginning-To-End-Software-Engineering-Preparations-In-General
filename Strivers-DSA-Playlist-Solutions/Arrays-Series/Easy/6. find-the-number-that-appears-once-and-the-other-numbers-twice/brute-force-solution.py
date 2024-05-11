# Time Complexity: O(n^2)
# Space Complexity: O(1)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            count = 0
            for j in range(n):
                if nums[i] == nums[j]:
                    count += 1
            if count == 1:
                return nums[i]
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 3, 2, 4, 1, 3, 2]))