"""
递归，创建全局变量，遍历树，遇到左子树就加到里面
"""
class Solution:
    def sumOfLeaves(self, root):
        if not root:
            return 0
        self.sum = 0
        self.inOrder(root)
        return self.sum

    def inOrder(self, root):
        if not root:
            return
        if root.left:
            self.inOrder(root.left)
            if not root.left.left and not root.left.right:
                self.sum += root.left.val
        if root.right:
            self.inOrder(root.right)

"""
树的问题一般都可以iteration或者recursion，本题用迭代的话要用栈
"""
class Solution:
    def sumOfLeftLeaves(self, root):
        if not root:
            return 0
        stack = []
        stack.append(root)
        leftsum = 0
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.left:
                if not node.left.left and not node.left.right:
                    leftsum += node.left.val
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return leftsum

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

        
        
