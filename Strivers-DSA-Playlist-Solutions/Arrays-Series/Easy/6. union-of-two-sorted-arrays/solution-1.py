# Solution using two pointers approach
# Time Complexity: O(n+m)
# Space Complexity: O(n+m)

class Solution:
    def findUnion(self,arr1,arr2,n,m):
        i, j = 0, 0
        union = []
        while (i < n and j < m):
            if (arr1[i] <= arr2[j]):
                if (len(union) == 0 or union[-1] != arr1[i]):
                    union.append(arr1[i])
                i += 1
            else:
                if (len(union) == 0 or union[-1] != arr2[j]):
                    union.append(arr2[j])
                j += 1

        while (i < n):
            if (union[-1] != arr1[i]):
                union.append(arr1[i])
            i += 1

        while (j < m):
            if (union[-1] != arr2[j]):
                union.append(arr2[j])
            j += 1

        return union
    
if __name__ == "__main__":
    s = Solution()
    arr1 = [1, 2, 2, 3, 4]
    arr2 = [2, 2, 4, 6]
    n = 5
    m = 4
    print(s.findUnion(arr1, arr2, n, m))