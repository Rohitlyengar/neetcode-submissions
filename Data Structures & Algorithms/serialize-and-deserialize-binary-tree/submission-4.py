# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        
        def DFS(root):
            if root:
                res.append(str(root.val))
                DFS(root.left)
                DFS(root.right)
            else:
                res.append('N')
        DFS(root)
        return ','.join(res)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(',')
        i = 0

        def DFS() -> Optional[TreeNode]:
            nonlocal i
            if vals[int(i)] == 'N':
                i += 1
                return
            root = TreeNode(vals[int(i)])
            i += 1
            root.left = DFS()
            root.right = DFS()

            return root

        return DFS()
