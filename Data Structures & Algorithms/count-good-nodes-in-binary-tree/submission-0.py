# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def DFS(root: Optional[TreeNode], curr: int) -> None:
            nonlocal count
            if root:
                if curr <= root.val:
                    count += 1
                DFS(root.left, max(curr, root.val))
                DFS(root.right, max(curr, root.val))
        DFS(root, root.val)
        return count
        