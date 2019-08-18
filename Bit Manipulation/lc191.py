"""
先转2进制然后数1
"""
class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
