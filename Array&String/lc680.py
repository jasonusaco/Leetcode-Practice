"""
双指针法
"""
class Solution:
    def validPalindrome(self, s):
        #定义左右指针
        left = 0
        right = len(s) - 1
        #双指针停止条件
        while left < right:
            if s[left] != s[right]:
                one = s[left:right]
                two = s[left+1:right+1]
                return one == one[::-1] or two == two[::-1]
            left = left + 1
            right = right - 1
        return True
            
