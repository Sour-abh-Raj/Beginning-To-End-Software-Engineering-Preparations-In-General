# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=7pnhv842keE

# Naive Approach
# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         res, maxCnt = 0, 0
#         cnt = {}
#         for n in nums:
#             cnt[n] = 1 + cnt.get(n, 0)
#             res = n if cnt[n] > maxCnt else res
#             maxCnt = max(cnt[n], maxCnt)
#         return n

# Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, cnt = 0, 0
        for num in nums:
            if cnt == 0:
                res = num
            cnt += (1 if num == res else -1)
        return res
