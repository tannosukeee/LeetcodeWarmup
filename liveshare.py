"""
Understand:
- Input: root/TreeNode
- Output: boolean
- Check if the subtrees are mirror or not

Match: Binary Tree

Plan:

- define a helper function, take 2 TreeNode stands for left and right
- if left is None and right is None then return True
- if left is None or right is None then return False
- if left value not equal to right value then return False
- return helper(left.left, right.right) and helper(left.right, right.left)

- define a function, take root
- if root is None then return False
- return helper(root.left, root.right)

Implement:
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(left, right):
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if left.val != right.val:
        return False
    return helper(left.left, right.right) and helper(left.right, right.left)
    
def is_symmetric(root):
    if root is None:
        return False
    return helper(root.left, root.right)
