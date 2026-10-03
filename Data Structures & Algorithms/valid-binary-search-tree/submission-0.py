# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')
        flag = True

        def DFS(root: Optional[TreeNode]) -> None:
            nonlocal prev, flag
            if root:
                DFS(root.left)
                if prev >= root.val:
                    flag = False
                prev = root.val
                DFS(root.right)
        
        DFS(root)
        return flag

        