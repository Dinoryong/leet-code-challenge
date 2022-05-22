# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = deque()

        if root: q.append(root)

        while q:
            node = q.popleft()

            if node.left and node.right:
                q.append(node.left)
                q.append(node.right)

            else:
                if node.left:
                    q.append(node.left)
                    res.append(node.left.val)
                elif node.right:
                    q.append(node.right)
                    res.append(node.right.val)

        return res