"""
暴力解，由于x+y不能大于12，所以不用担心递归超时问题
直接列出特殊情况，x或y等于0,x或y等于1的时候，其他情况直接
递归,x-1是向下走的所有走法，y-1是向右走的所有走法，加起来就是
全部走法
"""
class Robot:
    def countWays(self,x,y):
        if x == 0 or y == 0:
            return 0
        elif x == 1 or y == 1:
            return 1
        else:
            return self.countWays(x,y-1)+self.countWays(x-1,y)
        
    
