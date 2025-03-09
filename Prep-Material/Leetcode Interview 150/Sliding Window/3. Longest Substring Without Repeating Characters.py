# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=wiGpQwVHdE0

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, res = 0, 0
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res