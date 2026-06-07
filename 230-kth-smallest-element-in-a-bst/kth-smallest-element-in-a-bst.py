# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        
        result = []

        def inorder(node):

            if not node:
                return None

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        return result[k-1]
