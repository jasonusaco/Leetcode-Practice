"""
对于数字1，后面的一个数字是1或者0都行，所以遇到可以跳过1后面的值
遇到0，则移动一位
"""
class Solution(object):
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 2
                if i == len(bits):
                    return False
            else:
                i += 1
        return True
