# https://leetcode.com/problems/linked-list-cycle/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=gBTe7lFR3vc

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Using Floyd's Tortoise and Hare algorithm
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        