"""
简单切片
"""
class Solution:
    def reverseStr(self, s, k):
        res = ''
        pos = 0
        while pos < len(s):
            start = s[pos:pos+k]
            res = res + start[::-1] + s[pos+k:pos+2*k]
            pos += 2*k
        return res
