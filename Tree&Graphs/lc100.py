# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
先判断特殊情况，如果p和q都是空的，那么也是true
然后就是递归判断p和q的左右子树是否分别都相等
"""

class Solution:(object):
    def isSameTree(self,p,q):
        if p == None:
            return q == None
        if q == None:
            return p == None
        if p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
