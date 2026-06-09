# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def depth(node):

            if not node:
                return 0

            rightL = depth(node.right)
            if rightL == -1:
                return -1
            leftL = depth(node.left)
            if leftL == -1:
                return -1

            if abs(leftL - rightL) > 1:
                return -1

            return max(leftL, rightL) + 1

        return depth(root) != -1