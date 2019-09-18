class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def dfs(root):
            if not root:
                return 0
            #遍历左右子树
            left = dfs(root.left)
            right = dfs(root.right)
            #路径是当前节点左右子树深度的和
            self.ans = max(self.ans, left+right)
            return max(left,right)+1
        dfs(root)
        return self.ans
            
