# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
如果根节点为空，那么返回0，如果左子树为空，返回右子树的最低高度+1，
右子树为空，返回左子树最低高度+1，
否则返回min(左子树最低高度，右子树最低高度）+1
"""

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        elif root.left == None:
            return minDepth(root.right)+1
        elif root.right == None:
            return minDepth(root.left)+1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right))+1
        
