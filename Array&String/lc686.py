"""
不断重复A，当A比B长了，判断一次B是不是substring，
如果不是，再重复一次A，在判断，如果还不是，直接返回-1
"""
class Solution:
    def repeatedStringMatch(self, A, B):
        lenB = len(B)
        res = A
        count = 1
        while len(res) < lenB:
            res += A
            count += 1
        if res.find(B) != -1:
            return count
        res += A
        if res.find(B) != -1:
            return count + 1
        return -1
