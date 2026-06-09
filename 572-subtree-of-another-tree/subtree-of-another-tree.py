# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        
        def checker(root, subroot):
            if not root and not subroot:
                return True

            if not root or not subroot or root.val != subroot.val:
                return False

            return checker(root.left, subroot.left) and checker(root.right, subroot.right)
        
        if not root:
            return False

        if checker(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
