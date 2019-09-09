"""
首先弄清楚n叉树的数据结构，val是节点的值，children是列表
用于保存其所有节点，题目是标准的先进先出的结构，所有用queue实现
由于每层都在一个list中，所以在进入队列的时候需要保存一下这个节点属于哪个层
这样当遍历它的时候，就能直接放入它那层的list的末尾
"""
class Solution:
    def levelOrder(self, root):
        #特殊情况直接返回空列表
        if not root:
            return []
        #建立队列
        queue = [(root, 0)]
        #储存结果的二维数组
        res = [[]]
        while queue:
            node, level = queue.pop(0)
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            for child in node.children:
                queue.append((child, level+1))
        return res


        
        
