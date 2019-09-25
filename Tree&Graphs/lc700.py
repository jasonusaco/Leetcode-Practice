"""
只要是BST查找，那肯定都好说。树的查找比较简单的就是递归，如果节点是空，那么肯定没找到；
节点值相等，返回这个节点；如果节点值小于要查找的值，
那么在当前节点的右子树中找；否则在左子树中找。
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        if root.val == val:
            return root
        elif root.val < val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)
