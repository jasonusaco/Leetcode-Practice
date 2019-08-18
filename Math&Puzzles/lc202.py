"""
循环计算各位平方和，观察是否收敛到1,
为了避免重复，建一个dict来保存已出现的数字
"""
class Solution:
    def isHappy(self, n):
        dict = []
        while True:
            sum = 0
            while n > 0:
                #
                sum += (n%10)**2
                n = int(n/10)
            n = sum
            if sum == 1:
                return True
            elif sum in dict:
                return False
            else:
                dict.append(sum)
