"""
先比较左右子树然后递归
"""
class Solution:
    def isSymmetrical(self, pRoot):
        if not pRoot:
            return True
        def Traversal(left, right):
            if left is None and right is None:
                return True
            elif left and right and left.val == right.val:
                return Traversal(left.left, right.right) and Traversal(left.right, right.left)
            else:
                return False
        return Traversal(pRoot.left, pRoot.right)
