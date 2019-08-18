# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
DFS）递归算法，每次递归交换当前节点的左右子树，同时对左右子树做同样的处理。
"""
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.left or root.right:
            temp = root.left
            root.left = self.invertTree(root.right)
            root.right = self.invertTree(temp)
        return root
