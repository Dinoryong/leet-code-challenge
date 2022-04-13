# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self, root, subroot):
        if not root and not subroot:
            return True
        if not root or not subroot:
            return False
        return root.val == subroot.val and self.same(root.left, subroot.left) and self.same(root.right, subroot.right)
    
    def checksubtree(self, cur, subRoot) -> bool:
        if not cur:
            return False
        if self.same(cur, subRoot):
            return True
        else:
            return self.checksubtree(cur.left, subRoot) or self.isSubtree(cur.right, subRoot)
              
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.checksubtree(root, subRoot)