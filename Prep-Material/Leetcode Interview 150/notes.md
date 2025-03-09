# 1. Algorithms for Tree Traversal

## Inorder(tree) 
 - Traverse the left subtree, i.e., call Inorder(left->subtree) 
 - Visit the root. 
 - Traverse the right subtree, i.e., call Inorder(right->subtree)

## Preorder(tree) 
 - Visit the root. 
 - Traverse the left subtree, i.e., call Preorder(left->subtree) 
 - Traverse the right subtree, i.e., call Preorder(right->subtree) 

## Postorder(tree) 
 - Traverse the left subtree, i.e., call Postorder(left->subtree) 
 - Traverse the right subtree, i.e., call Postorder(right->subtree) 
 - Visit the root 