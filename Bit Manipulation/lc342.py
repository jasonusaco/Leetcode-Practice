"""
Power of X的万能解法，取余
如果每次将这个数除以x没有余数，直到得到数字1，
那么这个数就是x的若干次幂。
"""
class Solution:
    def isPowerOfFour(self, num):
        if num:
            while num % 4 == 0:
                num /= 4
            return num == 1
        return False
