# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=hTM3phVI6YQ

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Recursive DFS
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Iterative BFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         if not root:
#             return 0
#         level = 0
#         q = deque([root])
#         while q:
#             for i in range(len(q)):
#                 node = q.popleft()
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             level += 1
#         return level

# Iterative DFS
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         stack = [[root, 1]]
#         res = 0
#         while stack:
#             node, depth = stack.pop()
#             if node:
#                 res = max(res, depth)
#                 stack.append([node.left, depth + 1])
#                 stack.append([node.right, depth + 1])
#         return res
