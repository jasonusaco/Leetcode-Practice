"""
先遍历树1，找到树1中与树2根节点值相等的节点
说明可能就是子结构的根
然后检查以此节点为根的树3，是否包含树2中的结构
"""
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 and pRoot2:
            #根节点相同的话就调用检查结构的方法
            if pRoot1.val == pRoot2.val:
                result = self.check_structure(pRoot1, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def check_structure(self, root1, root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        #检查左边
        left_check = self.check_structure(root1.left, root2.left)
        right_check = self.check_structure(root1.right, root2.right)
        return left_check and right_check
        
