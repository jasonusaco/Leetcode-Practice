"""
当中序遍历时，如果节点是叶子节点则放入序列之中
然后判断两棵树的序列是否相等即可
"""
class Solution:
    def leafSimilar(self, root1, root2):
        leaves1 = []
        leaves2 = []
        self.inOrder(root1, leaves1)
        self.inOrder(root2, leaves2)
        return leaves1 == leaves2

    def inOrder(self, root, leaves):
        if not root:
            return
        self.inOrder(root.left, leaves)
        if not root.left and not root.right:
            leaves.append(root.val)
        self.inOrder(root.right, leaves)
