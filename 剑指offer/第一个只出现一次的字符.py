"""
开一个额外的数组，存入只出现一次的元素
然后返回第一个即可
"""
class Solution:
    def FirstNotRepeatingChar(self, s):
        if len(s) == 0:
            return -1
        if len(s) == 1 or len(s) == 2:
            return 0
        a = []
        for i in s:
            if s.count(i) == 1:
                a.append(i)
        return s.index(a[0])
