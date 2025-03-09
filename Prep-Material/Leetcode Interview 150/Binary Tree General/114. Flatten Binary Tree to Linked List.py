# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=rKnD7rLT0lI

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        while root:
            if root.left:
                rightmost = root.left
                while rightmost.right:
                    rightmost = rightmost.right
                rightmost.right = root.right
                root.right = root.left
                root.left = None
            root = root.right
        