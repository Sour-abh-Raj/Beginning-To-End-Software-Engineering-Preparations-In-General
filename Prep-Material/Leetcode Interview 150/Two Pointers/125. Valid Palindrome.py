# https://leetcode.com/problems/valid-palindrome/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=jJXJ16kPFWg

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        return cleaned == cleaned[::-1]

# import re

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
#         return cleaned == cleaned[::-1]

# isPalindrome = lambda s: (cleaned := ''.join(filter(lambda x: x.isalnum(), s)).lower() == cleaned[::-1].lower()