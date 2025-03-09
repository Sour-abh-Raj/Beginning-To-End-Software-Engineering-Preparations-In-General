# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
# https://www.youtube.com/watch?v=U4hFQCa1Cq0

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        curr = root
        while curr.left:
            temp = curr
            while temp:
                temp.left.next = temp.right
                if temp.next:
                    temp.right.next = temp.next.left
                temp = temp.next
            curr = curr.left
        return root

# Two pointer approach. One for current level and one for next level.
# class Solution:
    # def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
    #     node = root
    #     curr, nxt = node, node.left if node else None
    #     while curr and nxt:
    #         curr.left.next = curr.right
    #         if curr.next:
    #             curr.right.next = curr.next.left
    #         curr = curr.next
    #         if not curr:
    #             curr = nxt
    #             nxt = curr.left
    #     return node
    