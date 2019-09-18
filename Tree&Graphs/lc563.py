"""
后序遍历，用一个res来保存左右子树差的结果
函数的返回值是左右子树的和加上根节点的值
"""
class Solution:
    def findTilt(self, root):
        self.sums = 0
        self.postOrder(root)
        return self.sums

    def postOrder(self, root):
        if not root:
            return 0
        left = self.postOrder(root.left)
        right = self.postOrder(root.right)
        self.sums += abs(left - right)
        return left+right+root.val
