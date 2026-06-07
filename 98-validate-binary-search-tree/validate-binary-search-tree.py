# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        
        def validate(node, min_value, max_value):

            if not node:
                return True

            if not (min_value < node.val < max_value):
                return False

            left_valid = validate(node.left, min_value, node.val)
            right_valid = validate(node.right, node.val, max_value)

            return left_valid and right_valid

        return validate(root, float('-inf'), float('inf'))