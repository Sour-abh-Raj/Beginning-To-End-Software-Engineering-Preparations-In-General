# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=99RVfqklbCE

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return True if i == len(s) else False