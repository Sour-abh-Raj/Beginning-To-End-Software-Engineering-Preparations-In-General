# For each element in the nums array we are trying to find the same element in the nums array using nums linear search.
# If we don't find any elemnt in the nums array, we return that element.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n + 1):
            flag = 0
            for j in range(n):
                if nums[j] == i:
                    flag = 1
                    break
            if flag == 0:
                return i
        return -1
    
if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(arr))