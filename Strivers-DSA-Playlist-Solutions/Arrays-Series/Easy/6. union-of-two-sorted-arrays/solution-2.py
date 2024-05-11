# Solution using Hashing with ordered map
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution:
    def findUnion(self,arr1,arr2,n,m):
        freq = {}
        union = []
        for num in arr1:
            freq[num] = freq.get(num, 0) + 1
        for num in arr2:
            freq[num] = freq.get(num, 0) + 1
        for num in freq:
            union.append(num)
        return union

if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6]
    n = 5
    m = 4
    print(s.findUnion(arr1, arr2, n, m))