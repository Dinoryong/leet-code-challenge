# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sums = 0
        self.val = None   # 记录找到的 node value
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node: Optional[TreeNode]) :
            if node is None : 
                return
            traverse(node.right)
            
            self.sums = self.sums + node.val
            node.val = self.sums
            traverse(node.left)

            # return self.val
        traverse(root)
        return root