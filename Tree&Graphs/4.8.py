"""
满二叉树的子节点与父节点的关系为root = child/2
利用这个关系，如果a != b,就让其中的较大数除以2，如此循环直到a == b,
就是两个数的最近公共祖先了
"""
class LCA:
    def getLCA(self,a,b):
        while a != b:
            if a > b:
                a /= 2
            elif a < b:
                b /= 2
            else:
                break
        return a
