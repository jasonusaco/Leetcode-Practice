"""
题目本质上是一个十进制转二十六进制的问题
"""
class Solution:
    def convertToTitle(self, n):
        res = ''
        while n:
            res = chr((n-1)%26 + 65) + res
            n = (n-1) / 26
        return res
        
