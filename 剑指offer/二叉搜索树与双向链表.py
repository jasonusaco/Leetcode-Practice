class Solution:
    def Convert(self, pRootOfTree):
        if not pRootOfTree:
            return None
        newRoot = self.visit(pRootOfTree)
        # 注意这里：递归返回的是整个双向链表的最大值节点，题目要求返回头节点（最小值）
        while(newRoot.left):
            newRoot = newRoot.left
        return newRoot
    # 递归遍历    
    def visit(self, root):
        right_max = None
        if not root:
            return None
        # 先递归左子树
        if root.left:
            # 递归左子树，返回值是左子树的最大节点
            left = self.visit(root.left)
            # 修改根节点和left的指向
            left.right = root
            root.left = left
        # 再递归右子树
        if root.right:
            # 递归右子树，返回值是右子树的最大节点
            right = self.visit(root.right)
            # 向左寻找最小值之前，先记下最大值，后面return要用
            right_max = right
            # 修改根节点和right的指向
            while(right.left):
                right = right.left
            right.left = root
            root.right = right
        # 返回最大值
        if right_max:
            return right_max
        else:
            return root
