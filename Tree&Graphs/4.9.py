"""
递归问题，首先特殊情况，当为空树或者不存在子节点时，返回空
如果存在子节点，判断以子节点为根的二叉树是否能找到和为
【原期望值-原根节点值】的路径，如果存在返回路径列表，如果不存在
返回空列表,由于是左右两边遍历，所以遍历完返回的列表需要合并，
合并出来的列表只要不为空，说明有路径存在，那么在列表基础上加上root的值即可
"""

class Solution:
    def FindPath(self, root, expectNumber):
        #空树的情况，返回空列表
        if not root:
            return []
        
        #如果不存在子节点
        if root.left is None and root.right is None:
            #根节点如果和期望值一样，就返回根节点的二维数组
            if root.val == expectNumber:
                return [[root.val]]
            else:
                #如果根节点也和期望值不一样，就说明不存在路径
                #返回空列表
                return []
            
        #上面是特殊情况，以下是正常情况的处理方式
        else:
            #定义两个列表用于遍历左右子树
            pathl = []
            pathr = []
            #如果左右树不为空，递归遍历
            if root.left is None:
                pathl = self.FindPath(root.left, expectNumber - root.val)
            if root.right is None:
                pathr = self.FindPath(root.right, expectNumber - root.val)
            #合并左右两边遍历出的结果列表
            path = pathl + pathr
            if path:
                for each in path:
                    #在合并列表的基础上加上root的值
                    each.insert(0,root.val)
            return path
