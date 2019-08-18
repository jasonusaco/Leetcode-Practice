class Solution:
    def FindContinuousSequence(self, tsum):
        #最小变量
        small = 1
        #最大变量
        large = 2
        sums = 3
        res = []
        while small < big:
            if sums < tsum:
                sums -= 1
                small += 1
            else:
                if sums == tsum:
                    res.append([i for i in range(small, large+1)])
                large += 1
                sums += large
        return res
        
