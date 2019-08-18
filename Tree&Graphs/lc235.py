# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
首先BST的定义是左子树小于根节点小于右子树
递归算法：
从根节点开始遍历，如果p和q都是右子树（都比根节点大），那么递归遍历
如果都是左子树，同样
如果遍历左子树和右子树的条件都为false，说明找到了lca，直接返回
时间复杂度和空间复杂度都是O(n)
"""
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right,p,q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root
