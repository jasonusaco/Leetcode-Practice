"""
平衡二叉树是通过左右子树的高度来判断的，
求树的高度直接用递归，每次求出左右子树的最大高度再加一
就是父节点的高度，这样递归下去，便可以求出任何一棵树的高度
"""
class Balance:
    def isBalance(self, root):
        if root is None:
            return True
        leftHeight = self.getHeight(root.left)
        rightHeight = self.getHeight(root.right)
        if leftHeight - rightHeight > 1 or rightHeight - leftHeight > 1:
            return False
        return True

    def getHeight(self,root):
        if root is None:
            return 0
        #递归求出左子树的高度
        leftHeight = 1 + self.getHeight(root.left)
        #递归求出右子树的高度
        rightHeight = 1 + self.getHeight(root.right)
        return max(leftHeight, rightHeight)
