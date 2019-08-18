class Solution(object):
    def minDiffInBST(self, root):
        self.res = []
        #最大可能
        self.min_diff = float("inf")
        #持续记录之前的元素
        self.prev = None
        #因为中序遍历是按照升序来的，left，root，right
        self.inorder(root)
        return self.min_diff

    def inorder(self, root):
        if not root:
            return

        self.inorder(root.left)
        if self.prev != None:
            #取之前值和现在值之间最小的
            self.min_dif = min(self.min_diff, abs(self.prev-root.val))
        #把当前的value存下来用于和下一个中序值比较
        self.prev = root.val
        self.inorder(root.right)
        
