class Solution:
    def binaryGap(self, N):
        #先求出二进制
        binary = bin(N)[2:]
        index = -1
        res = 0
        for i, b in enumerate(binary):
            #统计二进制中每个1里左边1的距离
            if b == '1':
                if index != -1:
                    res = max(res, i-index)
                index = i
        return res
