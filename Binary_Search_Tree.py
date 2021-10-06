#Write a Python program
# to create a Balanced Binary Search Tree (BST)
#  using an array (given) elements
# where array elements are
# sorted in ascending order.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid_val = len(nums)//2
    node = TreeNode(nums[mid_val])
    node.left = TreeNode(nums[:mid_val])
    node.right = TreeNode(nums[mid_val + 1:])
    return node


def PreOrder(node):
    if not node:
        return
    print(node.val)
    PreOrder(node.left)
    PreOrder(node.right)



result = sorted_array_to_bst([1,2,3,4,5,6,7])

PreOrder(result)

