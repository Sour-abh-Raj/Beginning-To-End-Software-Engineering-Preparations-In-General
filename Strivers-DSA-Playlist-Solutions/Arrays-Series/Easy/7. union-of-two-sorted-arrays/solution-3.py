# Solution using Hashing with ordered set
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution:
    def findUnion(self,arr1,arr2,n,m):
        s = set()
        union = []
        for num in arr1:
            s.add(num)
        for num in arr2:
            s.add(num)
        for num in s:
            union.append(num)
        return union

if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6]
    n = 5
    m = 4
    print(s.findUnion(arr1, arr2, n, m))