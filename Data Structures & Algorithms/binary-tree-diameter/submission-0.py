# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def DFS(root):
            nonlocal res
            if root:
                x = DFS(root.left)
                y = DFS(root.right)
                res = max(res, x + y)
                return max(x, y) + 1
            return 0
        DFS(root)
        return res