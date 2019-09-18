"""
方法1，递归，先修改数值大的节点，再修改数值小的，这样
才能一次遍历就全部囊括，
bst的右子树都比该节点大，所以修改次序是right,root,left
用一个变量储存遍历过程中所有节点之和就得到了所有的比当前把该节点
的值更大的和，然后修改为该变量即可
"""
class Solution:
    def convertBST(self, root):
        #和的初始值为0
        self.sum = 0
        def afterOrder(cur):
            if not cur:
                return
            #遍历右节点
            afterOrder(cur.right)
            #把值加到sum里面
            self.sum += cur.val
            #再把sum值赋给当前节点
            cur.val = self.sum
            #然后遍历左子树
            afterOrder(cur.left)
        #调用方法
        afterOrder(root)
        #返回树
        return root

"""
方法2，非递归，还是采用right-root-left的顺序，用stack实现
"""
class Solution2:
    def convertBST(self, root):
        stack = []
        pNode = root
        sums = 0
        while(pNode or len(stack)):
            if pNode:
                stack.append(pNode)
                pNode = pNode.right
            else:
                pNode = stack.pop()
                pNode.val += sums
                sums = pNode.val
                pNode = pNode.left
        return root
        
