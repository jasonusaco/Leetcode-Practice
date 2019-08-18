class Solution:
    def LeftRotateString(self, s, n):
        #直接反转，最简单的方式
        return s[n:]+s[:n]
