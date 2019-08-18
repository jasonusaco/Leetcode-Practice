"""
由于有特殊情况，负数和反过来是0开头的
建立一个flag作为符号位，初始值等于1，如果检测到x是小于0的
就把flag赋值为-1，x%10可以获得末位数
"""
class Solution:
    def reverse(self,x):
        result = 0
        flag = 1
        if x < 0:
            flag = -1
            x *= -1
        while (x!=0):
            result = result * 10 + x%10
            x /= 10
        return result * flag

"""
作弊式解法
"""
class Solution:
    def reverse(self, x):
        if x < 0:
            result = -int(str(-x)[::-1])  # 字符串倒序输出
        else:
            result = int(str(x)[::-1])
        if result < -2147483648 or result > 2147483647:
            return 0
        return result
