class Solution:
    def leaders(self, A, N):
        sol = []
        for i in range(N):
            leader = True
            for j in range(i+1, N):
                if (A[j] > A[i]):
                    leader = False
                    break
            if leader:
                sol.append(A[i])
        return sol