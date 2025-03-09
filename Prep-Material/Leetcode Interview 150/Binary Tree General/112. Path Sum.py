# https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=LSKQyOz_P8I

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False
            currSum += node.val
            if not node.left and not node.right:
                return currSum == targetSum
            return (dfs(node.left, currSum) or dfs(node.right, currSum))
        return dfs(root, 0)