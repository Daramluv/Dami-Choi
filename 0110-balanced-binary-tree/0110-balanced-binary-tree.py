# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        if abs(left_depth - right_depth) <= 1:
            return self. isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False
    
    def maxDepth(self, root):
        if root is None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return 1 + max(left_depth, right_depth)