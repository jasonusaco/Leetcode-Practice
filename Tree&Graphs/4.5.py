"""
如果一个二叉树满足：对于任意一个节点，其值不小于左子树的任何节点，
且不大于右子树的任何节点（反之亦可），则为二叉搜索树
inorder遍历是按照升序访问节点的，所以这里可以inorder遍历bst
然后把结果存放在一个数组里面，最后判断这个数组是否为有序数组
是的话就是bst，不是的话就不是
"""
class Checker:
    def checkBST(self,root):
        #用于存放遍历结果
        self.arr = []
        self.dfs(root)
        return self.arr == sorted(self.arr)

    #中序遍历
    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)
