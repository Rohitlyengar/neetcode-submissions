# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def DFS(root: Optional[TreeNode], curr: int) -> None:
            nonlocal res
            if root:
                if root.val >= curr:
                    res += 1
                DFS(root.left, max(root.val, curr))
                DFS(root.right, max(root.val, curr))
        DFS(root, root.val)
        return res

        