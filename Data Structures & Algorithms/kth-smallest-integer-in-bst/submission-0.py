# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0

        def DFS(root: Optional[TreeNode]) -> None:
            nonlocal k, res
            if root:
                DFS(root.left)
                k -= 1
                if k == 0:
                    res = root.val
                    return
                DFS(root.right)

        DFS(root)
        return res
