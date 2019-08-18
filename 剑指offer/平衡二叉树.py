class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        #判断左右子树的深度是否一样，不一样直接false
        if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right))>1:
            return False
        #然后递归
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

    #分别求出左子树右子树的深度
    def TreeDepth(self,root):
        if root is None:
            return 0
        left=self.TreeDepth(root.left)
        right=self.TreeDepth(root.right)
        return max(left+1,right+1)
