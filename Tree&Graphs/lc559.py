"""
N叉树就是val为节点的值，children是一个列表，这个列表保存了其所有节点
求一个树的高度，完全可以转换成一个递归问题，树的高度= 1+子树最大高度
"""
class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.children:
            return 1
        depth = 1 + max(self.maxDepth(child) for child in root.children)
        return depth
