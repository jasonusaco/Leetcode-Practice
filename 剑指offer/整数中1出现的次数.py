"""
直接遍历的过程中把每个数转成str，然后判断是否有1，有的话count+1
最后返回count
"""
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        count = 0
        for i in range(0, n+1):
            for j in str(i):
                if j == '1':
                    count += 1
        return count
