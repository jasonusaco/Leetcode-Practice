"""
弱鸡转换法，先转成int，乘完再转回string
"""
class Solution:
    def multiply(self, num1, num2):
        a = int(num1)
        b = int(num2)
        return str(a*b)


        
