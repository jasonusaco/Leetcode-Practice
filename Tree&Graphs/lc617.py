"""
当t1 t2都是none的时候，返回空，如果只有t1是none，返回t2，反之
t1和t2的val不断相加，把t2加到t1上
分别递归左子树和右子树
最后返回t1
"""
class Solution:
    def mergeTrees(self, t1, t2):
        if t1 == None and t2 == None:
            return
        if t1 == None:
            return t2
        if t2 == None:
            return t1
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left, t2.left)
        t1.right = self.mergeTrees(t1.right, t2.right)
        return t1
