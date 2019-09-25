"""
暴力条件法
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            ones = int(i//1%10)
            tens = int(i//10%10)
            hundreds = int(i//100%10)
            thousands = int(i//1000%10)
            
            if i >=  1000 and i < 10000 and ones != 0 and tens != 0 and hundreds != 0 and thousands != 0:
                if i%thousands == 0 and i%hundreds == 0 and i%tens == 0 and i%ones == 0:
                    res.append(i)
                    
            elif i>= 100 and i < 1000 and hundreds != 0 and tens != 0 and ones != 0:
                if i%hundreds == 0 and i%tens == 0 and i%ones == 0:
                    res.append(i)
            
            elif i >= 10 and i < 100 and tens != 0 and ones != 0:
                if i%tens == 0 and i%ones == 0:
                    res.append(i)
                
            elif i >= 1 and i < 10 and ones != 0:
                if i%ones == 0:
                    res.append(i)
        return res

"""
写个判断方法
"""
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        for x in range(left, right+1):
            if self.is_self_dividing(x):
                ans.append(x)
        return ans
                    
    def is_self_dividing(self, x):
        #遍历范围的每个整数时，先转成字符串
        s = str(x)
        #然后方法中遍历字符串，如果任何一个字符等于0
        #或者对任何一个字符取余不等于0都是false
        for d in s:
            if d=="0" or x%int(d)!=0:
                return False
        return True
