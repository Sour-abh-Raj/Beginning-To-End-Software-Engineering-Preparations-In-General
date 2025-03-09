# https://leetcode.com/problems/symmetric-tree/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=Mao9uzxwvmc

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val == right.val and
                self.dfs(left.left, right.right) and
                self.dfs(left.right, right.left))
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)
        
