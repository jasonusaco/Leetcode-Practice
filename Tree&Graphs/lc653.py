class Solution:
    def findTarget(self, root, k):
        dic = {}
        return self.dfs(root, k, dic)

    def dfs(self, root, k, dic):
        if root == None:
            return False
        #存在一个值和当前值加起来等于k的话就说true
        if k - root.val in dic:
            return True
        else:
            #分别递归左右子树来查找
            dic[root.val] = 1
            return self.dfs(root.left, k, dic) or self.dfs(root.right, k, dic)
