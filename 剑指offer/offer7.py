"""
前序序列能确定根节点，使用根节点把中序划分为左右子树
然后递归重复上述步骤
"""
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        #前序遍历的第一个节点就是根节点
        root = TreeNode(pre[0])
        #确认中序遍历的根节点位置
        tin_root_index = tin.index(root.val)
        #左子树
        if tin_root_index > 0:
            new_tin = tin[0: tin_root_index]
            new_pre = pre[1:len(new_tin)+1]
            root.left = self.reConstructBinaryTree(new_pre, new_tin)
        #右子树
        if tin_root_index != len(tin) - 1:
            new_tin = tin[tin_root_index+1]
            new_pre = pre[len(pre)-len(new_tin):]
            root.right = self.reContructBinaryTree(new_pre, new_tin)
        return root
        
