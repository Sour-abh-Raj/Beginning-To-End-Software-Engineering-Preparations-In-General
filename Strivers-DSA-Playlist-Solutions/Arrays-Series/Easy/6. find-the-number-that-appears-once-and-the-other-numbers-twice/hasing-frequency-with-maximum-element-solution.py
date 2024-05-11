# Soultion using hashing the frequency of each element with maximum element + 1 size array
# We used maximum element + 1 size array because there's a missing element in the array
# Time: O(N)
# Space: O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        freq = [0] * (maximum + 1)
        for num in nums:
            freq[num] += 1
        for num in nums:
            if freq[num] == 1:
                return num
        # We could've also used:
        # for i in range(maximum + 1):
        #     if freq[i] == 1:
        #         return i
        return -1
    
if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 3, 2, 4, 1, 3, 2]))