# https://leetcode.com/problems/sum-root-to-leaf-numbers/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=5GfVu9QfbnU

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(node, currSum):
            if not node:
                return 0
            currSum = currSum * 10 + node.val
            if not node.left and not node.right:
                return currSum
            return dfs(node.left, currSum) + dfs(node.right, currSum)
        return dfs(root, 0)
        