"""
思路和反转一样，只是多个比较
"""
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        temp = x
        rev = 0
        while temp:
            rev = rev * 10 + temp % 10
            temp //= 10
        return rev == x
