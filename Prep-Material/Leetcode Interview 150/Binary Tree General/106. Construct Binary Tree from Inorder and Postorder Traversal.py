# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/?envType=study-plan-v2&envId=top-interview-150
# https://www.youtube.com/watch?v=vm63HuIU7kw

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorderIdx = {v:i for i, v in enumerate(inorder)}
        def helper(l: int, r: int):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderIdx[root.val]
            root.right = helper(idx + 1, r)
            root.left = helper(l, idx - 1)
            return root
        return helper(0, len(inorder) - 1)


# Without optimization
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not inorder:
#             return None
#         root = TreeNode(postorder.pop())
#         idx = inorder.index(root.val)
#         root.right = self.buildTree(inorder[idx+1:], postorder)
#         root.left = self.buildTree(inorder[:idx], postorder)
#         return root
        