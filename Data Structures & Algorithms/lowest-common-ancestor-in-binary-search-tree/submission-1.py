# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if q.val < root.val and p.val < root.val:
                root = root.left
            elif q.val > root.val and p.val > root.val:
                root = root.right
            else:
                return root