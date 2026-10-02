# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def DFS(root: Optional[TreeNode], curr: int) -> bool:
            if root:
                if root.left is None and root.right is None and root.val + curr == targetSum:
                    return True
                return DFS(root.left, curr + root.val) or DFS(root.right, curr + root.val)
            return False
        return DFS(root, 0)
