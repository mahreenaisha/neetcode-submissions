# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # in this function, find the node that matches and then pass it to isSameTree

        # imp distinction i caught: A subtree must contain all descendants of its root node. 
        # You cannot ignore extra children or descendants.

        # tc = o(m * n)
        # base case 1: if root node is null
        if not root:
            return False

        # base case 2: if subtree is null, it automatically is a subtree of the root tree
        if not subRoot:
            return True

        # base case: if nodes are equal and isSameTree is true, return true
        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        # base case: if root node doesnt exist, return false?? idk 

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

