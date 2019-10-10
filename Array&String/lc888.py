class Solution(object):
    def fairCandySwap(self, A, B):
        sum_A = sum(A)
        sum_B = sum(B)
        set_B = set(B)
        #算出两个数组和的平均数
        target = (sum_A + sum_B) / 2
        #对A数组进行遍历
        for a in A:
            #对于每一个数，得到出去该数以外其他的和然后用target减去这个和
            b = target - (sum_A - a)
            #然后看这个结果是否在数组B中，在的话就返回
            if b >= 1 and b <= 100000 and b in set_B:
                return [a,b]
