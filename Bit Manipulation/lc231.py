"""
n如果小于0，直接false
先把n转成二进制，然后如果里面只有一个1说明是2的次方数
"""
class Solution:
    def isPowerOfTwo(self,n):
        if n <= 0:
            return False
        return bin(n).count('1') == 1
