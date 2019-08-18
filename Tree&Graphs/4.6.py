"""
在中序遍历过程中，当某个节点的值等于p
则告诉递归下一个遍历的节点就是我们要找的节点
"""
class Successor:
    def findSucc(self, root, p):
        self.arr = []
        #中序遍历
        self.dfs(root)
        #返回p节点的index+1的节点的值
        return self.arr[self.arr.index(p) +1]

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.arr.append(root.val)
        self.dfs(root.right)
