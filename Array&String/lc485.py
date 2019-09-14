class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n = 0
        res = 0
        for i in nums:
            #每次用1来减去数组中的元素
            if i-1 == 0:
                #设置计数器来统计1的次数
                n += 1
                #返回次数最大值
                res = max(res,n)
            else:
                n = 0
        return res
