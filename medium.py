class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def bst_tree(nums):
    root = None
    for num in nums:
        if num is not None:
            root = insert(root, num)
    return root

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def findLCA(root, p, q):
    if root is None:
        return None
    if p < root.value and q < root.value:
        return findLCA(root.left, p, q)
    elif p > root.value and q > root.value:
        return findLCA(root.right, p, q)
    else:
        return root.value

nums = [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
p, q = 2, 4
root = bst_tree(nums)
l_value = findLCA(root, p, q)
print(f"The Lowest Common Ancestor of {p} and {q} is: {l_value}")
