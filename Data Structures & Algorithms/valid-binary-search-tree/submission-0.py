# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs, recursion
    # tc = o(n), sc = o(h) h = height of tree
    # maintain acceptable numeric value ranges for every node 
    # checking neighbouring nodes is not enough to validate a BST
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float("-inf"), float("inf"))
        
    def validate (self, node, left, right):
        if not node:
            return True

        if not (node.val > left and node.val < right):
            return False

        return (self.validate(node.left, left, node.val) and self.validate(node.right, node.val, right))

    