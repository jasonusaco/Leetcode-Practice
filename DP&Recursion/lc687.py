# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    #定义dfs函数通过root节点的情况下获取最长的单臂路径
    #其中更新的res是左右子树算上的
    def dfs(self,root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        pl = 0
        pr = 0
        if root.left and root.left.val == root.val:
            pl = left + 1
        if root.right and root.right.val == root.val:
            pr = right + 1
        self.res = max(self.res, pl+pr)
        return max(pl, pr)

"""
方法2
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
 
 
class Solution:
    def __init__(self):
        self.re = 0  # 用于记录每个节点的最长路径
 
    def longestUnivaluePath(self, root):
        def f(root, n):
            if root == None: return 0
            left = f(root.left, root.val)  # 获取左分支节点与当前节点的最长路径
            right = f(root.right, root.val)  # 获取右分支节点与当前节点的最长路径
            self.re = max(self.re, left + right)  # 获取当前节点的最长路径，并更新记录
            return max(left, right) + 1 if root.val == n else 0  # 当前节点与父节点的值是否相同，如果相同就在子节点加一
 
        f(root, 0)
        return self.re
