# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        def DFS(root: Optional[TreeNode]) -> int:
            if root:
                x = DFS(root.left)
                y = DFS(root.right)

                if x == -1 or y == -1 or abs(x - y) > 1:
                    return -1
                return 1 + max(x, y)
            return 0
        return DFS(root) != -1
