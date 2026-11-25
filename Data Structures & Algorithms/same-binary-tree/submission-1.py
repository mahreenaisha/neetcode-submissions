# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # dfs, recursive
        # tc = o(n), sc = o(n)

        # base case 1
        if not q and not p:
            return True

        # base case 2
        if not p or not q:
            return False

        # base case 3
        if (q.val != p.val):
            return False

        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))

            