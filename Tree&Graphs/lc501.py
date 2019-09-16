"""
二叉树的三种遍历方式中，本题一定是用中序，
因为只有中序才能将当前节点的值既算在左子树又算在右子树中
不会因为访问了左子树二对右子树造成影响
本题先中序遍历完以后得到有序的排列，如果两个相邻的元素相同
那么这个就是连续的，找出连续最多的即可
"""
class Solution(object):
    def findMode(self, root):
        if not root:
            return []
        #计数器,Counter方法是直接生成字典
        self.count = collections.Counter()
        #中序遍历得到有序的排列
        self.inOrder(root)
        freq = max(self.count.values())
        res = []
        #在count字典中遍历，如果和之前统计的频率一样就加入到res中
        for item, c in self.count.items():
            if c == freq:
                res.append(item)
        return res
    
    #中序遍历
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        self.count[root.val] += 1
        self.inOrder(root.right)
