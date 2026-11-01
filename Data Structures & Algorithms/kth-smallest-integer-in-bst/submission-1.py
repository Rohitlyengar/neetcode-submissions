# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = int()

        def DFS(root: Optional[TreeNode]) -> None:
            nonlocal k, res
            if root:
                DFS(root.left)
                if k == 1:
                    res = root.val
                k -= 1
                DFS(root.right)
        DFS(root)
        return res
