# Solution using hashing the frequency of each element
# Time: O(N)
# Space: O(N)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, value in freq.items():
            if value == 1:
                return key
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4, 3, 2, 4, 1, 3, 2]))