"""
暴力法，找出一个数的所有因数，存入数组
然后判断sum数组是否等于这个数
数小一点可以，大了会超时
"""
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        res = []
        a = 1
        while a <= num:
	        if num % a == 0:
		        res.append(a)
	        a = a + 1
        return sum(res[:-1]) == num

"""
用math.sqrt做
"""
from math import sqrt
class Solution(object):
    def checkPerfectNumber(self, num):
        #如果一个数小于2，一定不是perfect
        if num < 2:
            return False
        #从2开始遍历是为了防止把它本身也加进去，所以先把1加入到集合中
        divisor = {1}
        for i in range(2, int(sqrt(num)+1)):
            #取模等于0说明是因数
            if num % i == 0:
                divisor.add(i)
                divisor.add(num/i)
        return num == sum(divisor)
