"""
二叉搜索树的特点就是左子树比中间节点小
所有右子树都比中间节点大，这里是后续遍历
所以最后一个元素就是根节点，然后就这么递归下去
如果发现找不到左子树或者右子树就说明不对
"""
class Solution:
    de VerifySequenceOfBST(self, sequence):
        if not sequence:
            return False
        #找到根节点
        root = sequence[-1]
        split = len(sequence)-1

        #找到划分点
        for i in range(0, len(sequence)-1):
            if sequence[i] >= root:
                split = i
                break
            
        #确认后半段都比root大
        for i in range(split, len(sequence)-1):
            if sequence[i] <= root:
                return False

        #递归检查前半段和后半段
        left = True
        if split > 0:
            #前半段至少有两个元素，才递归
            left = self.VerifySequence(sequence[0:split])
        right = True
        if split < len(sequence)-1:
            #后半段同样也需要两个元素才能递归
            right = self.VerifySequenceOfBST(sequence[split:-1])
        return left and right
        
