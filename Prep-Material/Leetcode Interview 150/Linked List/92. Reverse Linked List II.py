# https://leetcode.com/problems/reverse-linked-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=RF_M9tX4Eag

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        lPrev, curr = dummy, head
        for _ in range(left - 1):
            lPrev, curr = curr, curr.next
        prev = None
        for _ in range(right - left + 1):
            tmpNext = curr.next
            curr.next = prev
            prev, curr = curr, tmpNext
        lPrev.next.next = curr
        lPrev.next = prev
        return dummy.next