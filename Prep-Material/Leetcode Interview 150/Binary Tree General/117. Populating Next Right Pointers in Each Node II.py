# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/?envType=study-plan-v2&envId=top-interview-150

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
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        curr = root
        dummy = Node(0)
        needle = dummy
        while curr:
            if curr.left:
                needle.next = curr.left
                needle = needle.next
            if curr.right:
                needle.next = curr.right
                needle = needle.next
            curr = curr.next
            if not curr:
                curr = dummy.next
                dummy.next = None
                needle = dummy
        return root