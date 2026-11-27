# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # dfs, recursion
        # tc = o(h) -> h = height of tree (H is much better than N)
        # sc = o(h)
        # why h? because we only explore one branch at a time. not all nodes. not right or left subtree.
        # base case of root being null is not needed as p and q are guaranteed to be descendants
        if (root.val > p.val and root.val > q.val):
            return self.lowestCommonAncestor(root.left, p, q)

        if (root.val < p.val and root.val < q.val):
            return self.lowestCommonAncestor(root.right, p, q)

        return root