"""
直接递归遍历左子树和右子树，取最大的
然后加上根节点即可
"""
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot is None:
            return 0

        left = self.TreeDepth(pRoot.left)
        right = self.TreeDepth(pRoot.right)
        return max(left, right)+1
