"""
暴力解，直接遍历
"""
class MagicIndex:
    def findMagicIndex(self, A, n):
        if not A:
            return False
        for i in range(len(A)):
            if A[i] == i:
                return True
            else:
                return False

"""
递归法+二分法
"""
class MagicIndex:
    def findMagicIndex(self, A, n):
        #0是start，n-1是end
        return self.find(A, 0, n-1)
    def find(self, A,start,end):
        #如果end小于等于start，直接报错
        while end <= start:
            return False
        #取中间数
        middle = (start+end)/2
        if A[middle] == middle:
            return True
        #如果中间数的index比中间数大，则说明魔术索引在左边
        #于是递归遍历start到middle
        if A[middle] > middle:
            return self.find(A,start,middle)
        #反之，则说明魔术索引在右边，递归遍历middle到end
        else:
            return self.find(A,middle,end)
        
