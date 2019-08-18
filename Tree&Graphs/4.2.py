"""
取数组的middle作为root，这样将数组分为两部分
又可以递归调用，邻节点是当数组被分割的只有2个或1个时，
无论怎么构造高度最低都为数组的长度，这时我们取
左子树的高度和右子树的高度的最大值，再加上根的高度，
就是最低高度，其实就是构造平衡二叉树
"""
class MinimalBST:
    #vals是一个有序序列int[]
    def buildMinimalBST(self,vals):
        if vals == None or len(vals) < 1:
            return 0
        return self.build(vals, 0, len(vals)-1)

    def build(self, vals, start, end):
        if end <= start:
            return 1
        mid = (start +end) // 2
        #左子树的高度+root的高度
        h1 = 1 + self.build(vals, start, mid-1)
        #右子树的高度+root的高度
        h2 = 1 + self.build(vals, mid+1, end)
        return max(h1,h2)


"""
方法2：高度最小，意味着是完全二叉树，
完全二叉树每个节点都有左右两个子节点，
所以直接看2的多少次方<节点数，返回那个多少次方即可
"""

def buildMinimalBST(self, vals):
    res = 0
    #vals的长度就是节点数
    while 2**res < len(vals):
        res += 1
    return res
