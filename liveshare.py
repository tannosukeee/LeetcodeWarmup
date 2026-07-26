#Problem 1

'''
1.Understand
Output: boolean so t or f
input: root/treenode
2. Match: Binary search
3.Plan
-define the function 
-check if there no treenode return false
- iterate through each node and check if the value is equal to the root value 
- return false if the current node value is not equal to the root value 
-keep iterating if current node value is true until reach the end and there is no node left
4. Implement
5. Review
6. Evaluate
'''
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def is_univalued_helper(root, value):
    if not root:
        return True
    if root.val != value:
        return False
    return is_univalued_helper(root.left, value) and is_univalued_helper(root.right, value)

def is_univalued(root):
    if not root:
        return False
    return is_univalued_helper(root.left, root.val) and is_univalued_helper(root.right, root.val)
# 5. Review
n1 = TreeNode(1)
n2 = TreeNode(1)
n3 = TreeNode(1)
n4 = TreeNode(1, n1, n2)
n5 = TreeNode(2, None, n3)
n6 = TreeNode(1, n4, n5)
 
print(is_univalued(n6))

'''
5: Evaluate
- Time complexity: O(n)
- Space complexity: O(n)
'''



'''
Understand:
-input :treenode
-output: integer
Match: binary search
Plan:
-define the function height()
-check if the root is none 
- if root is none return 0
- define left = height(root.left)
- define right = height(root.right)
- return 1 + max(height(root.left), height(root.right))
Implement
'''
class TreeNode():
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right
   
def height(root):
    if not root:
        return 0
    left = height(root.left)
    right = height(root.right)
    return 1 + max(left, right)

# Review
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(2, n1, n2)
n4 = TreeNode(5)
n5 = TreeNode(4, n3, n4)
print(height(n2)) 

'''
5: Evaluate
- Time complexity: O(n)
- Space complexity: O(n)
'''

'''
Understand
-input: root/treenode, key, value
-output: treenode
Match: binary search
Pln:
-define the function
-check if the root is none return TreeNode(key, value)
-if key < root.key then call insert(root.left, key, value)
-elif key > root.key then call insert(root.right, key, value)
-else then set root.val = value
-return root

Implement:
'''
class TreeNode():
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right
   
def insert(root, key, value):
    if not root:
        return TreeNode(key, value)
    if key < root.key:
        left = insert(root.left, key, value)
    elif key > root.key:
        right = insert(root.right, key, value)
    else:
        root.val = value
    return root

# Review
def print_tree(root, level=0, prefix="Root: "):
    if not root:
        return
    
    print(" " * (level * 4) + prefix + f"key={root.key}, val={root.val}")
    
    if root.left or root.right:
        if root.left:
            print_tree(root.left, level + 1, "L--- ")
        else:
            print(" " * ((level + 1) * 4) + "L--- None")
        
        if root.right:
            print_tree(root.right, level + 1, "R--- ")
        else:
            print(" " * ((level + 1) * 4) + "R--- None")


node1 = TreeNode(1, 'One')
node6 = TreeNode(6, 'Six')
node5 = TreeNode(5, 'Five', left=node1, right=node6)
node15 = TreeNode(15, 'Fifteen')
root = TreeNode(10, 'Ten', left=node5, right=node15)
print_tree(root)
root = insert(root, 9, 'Naruto')
print_tree(root)


#Done, make sure u copied all of them 

#thank you :)