# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
方法1：dfs,记录途中访问过的节点，遇到叶子节点可以生成一条路径字符串
记录路径的方法可以先保存在数组里，需要生成路径时在生成
也可以采用直接把目前为止的路径字符串保存下来
"""
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        #定义存放结果的数组和存放路径的数组
        res = []
        path_list = []
        return res

    def dfs(self, root, path_list, res):
        #还是先特殊情况，没得路径直接返回None
        if not root:
            return
        #把根节点的值以字符串的形式存入路径数组
        path_list.append(str(root.val))
        #直接返回根节点路径的情况
        if not root.left and not root.right:
            res.append('->'.join(path_list))
        if root.left:
            self.dfs(root.left, path_list, res)
        if root.right:
            self.dfs(root.right, path_list, res)
        path_list.pop()
