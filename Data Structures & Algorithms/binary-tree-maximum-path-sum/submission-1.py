# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def DFS(root: Optional[TreeNode]) -> int:
            nonlocal res
            if root:
                x = DFS(root.left)
                y = DFS(root.right)
                
                res = max(res, root.val, root.val + x, root.val + y, root.val + x + y)
                return max(root.val, root.val + x, root.val + y)
            return 0
        DFS(root)
        return res
        