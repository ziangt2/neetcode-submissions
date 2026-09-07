# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, high, low):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            
            left = dfs(node.left, node.val, low)
            right = dfs(node.right, high, node.val)

            return left and right 

        return dfs(root, float("inf"), float("-inf"))
