# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        #如果左子树和右子树都为空，就看看root的值是不是sum
        if  root.left == None and root.right == None:
            return root.val == sum

        if root.left == None:
            return self.hasPathSum(root.right, sum - root.val)

        if root.right == None:
            return self.hasPathSum(root.left, sum - root.val)
        
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - rot.val)
