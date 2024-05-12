# Solution using max element
# Time complexity: O(n)
# Space complexity: O(n)

class Solution:
    def leaders(self, A, N):
        sol = []
        maxSoFar = A[N - 1]
        sol.append(maxSoFar)
        for i in range(N - 2, -1, -1):
            curr = A[i]
            if curr >= maxSoFar:
                maxSoFar = curr
                sol.insert(0, curr)
        return sol