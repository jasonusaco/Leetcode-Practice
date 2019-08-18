"""
方法1：用collections的counter，统计两个string的字母个数
然后在大的string中遍历，遍历到不相等的index就返回

"""
class Solution:
    def findTheDifference(self, s, t):
        from collections import Counter
        cs = Counter(s)
        ct = Counter(t)

        for k in ct:
            if cs[k] != ct[k]:
                return k

            
