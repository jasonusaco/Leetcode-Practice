"""
把原输入字符串乘以2，然后去掉首尾
再判断原来的输入字符串是否在新字符串中
是的话就对了
"""
class Solution(object):
    def repeatedSubstringPattern(self, str):
        string = (str*2)[1:-1]
        return str in string
        
