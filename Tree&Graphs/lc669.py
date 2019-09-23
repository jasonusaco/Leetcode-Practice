class Solution:
    def trimBST(self, root, L, R):
        if not root:
            return
        #如果root的值比R大，说明root以及其所有右节点都不在这个区间内，则向左搜索
        if root.val > R:
            return self.trimBST(root.left, L, R)
        #如果root的值比L小，说明root以及其所有的左节点都不在这个区间内，则向右搜索
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        #如果在区间，则对左右子树进行收割
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
