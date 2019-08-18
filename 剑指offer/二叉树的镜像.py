"""
直接遍历每个节点，交换左右子树就行
"""
class Solution:
    def Mirror(self, root):
        if not root:
            return
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left, root.right = root.right, root.left
        return root
