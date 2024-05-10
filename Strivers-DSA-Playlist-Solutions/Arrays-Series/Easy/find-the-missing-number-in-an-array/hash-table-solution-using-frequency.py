# Since the array only has distinct elements, we caan use the frequency of each element to determine the missing number.
# We can use a hash table to store the frequency of each element in the array.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        hash = [0] * (n + 1)
        for i in range(n):
            hash[nums[i]] += 1
        for i in range(1, n + 1):
            if hash[i] == 0:
                return i
        return n
    
if __name__ == '__main__':
    arr = [9,6,4,2,3,5,7,0,1]
    s = Solution()
    print(s.missingNumber(arr))