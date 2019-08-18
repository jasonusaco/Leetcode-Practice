# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
对称的条件为：
两个节点值相等或者都为空
左节点的左子树和右节点的右子树相等
反之
"""
class Solution(object):
    def judge(self,p,q):
        #都为空
        if p == None and q == None:
            return True
        #两个节点值相等
        if p and q and p.val == q.val:
            #递归遍历
            return self.judge(p.left,q.right) and self.judge(p.right,q.left)
        return False
    
    def isSymmetric(self, root):
        if root:
            return self.judge(root.left, root.right)
        return True
