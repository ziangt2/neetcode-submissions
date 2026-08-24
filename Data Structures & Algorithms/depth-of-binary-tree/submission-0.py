# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        stack = [(root, 1)]
        maxd = 1
        d = 0
        while stack:
            node, d = stack.pop()
            maxd = max(maxd, d)

            if node.left:
                stack.append((node.left, d+1))
            if node.right:
                stack.append((node.right, d+1))

        return maxd

        
