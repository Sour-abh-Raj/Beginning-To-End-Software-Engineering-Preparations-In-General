# https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=5Y2EiZST97Y

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToNew = {None : None}
        if not head:
            return None
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToNew[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            node = oldToNew[curr]
            node.next = oldToNew[curr.next]
            node.random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]
        