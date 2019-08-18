"""
所有尾部的0都是2x5得来的，2的个数肯定是足够的
所以其实就计算5的个数即可
"""
class Solution(object):
    def trailingZeroes(self, n):
        res = 0
        while n > 0:
            n = int(n/5)
            res += n
        return res
