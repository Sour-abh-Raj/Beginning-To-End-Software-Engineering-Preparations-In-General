# Solution using set to store the visited elements
# Time complexity: O(n)
# Space complexity: O(n)
# Runtime : 37ms

class Solution:
    def findDuplicate(self, nums):
        visited = set()
        for num in nums:
            if num in visited:
                return num
            visited.add(num)
        return -1


if __name__ == "__main__":
    s = Solution()
    arr = [1, 3, 4, 2, 3]
    print("The duplicate element is ", s.findDuplicate(arr))