# https://leetcode.com/problems/binary-tree-maximum-path-sum/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=Hr5cWUld4vU

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 0
            lmax = dfs(node.left)
            rmax = dfs(node.right)
            lmax = max(lmax, 0)
            rmax = max(rmax, 0)
            res = max(res, node.val + lmax + rmax)
            return node.val + max(lmax, rmax)
        dfs(root)
        return res