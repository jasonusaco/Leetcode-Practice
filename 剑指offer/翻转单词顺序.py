class Solution:
    def ReverseSentence(self, s):
        a = s.split(' ')
        a.reverse()
        b = ' '.join(a)
        return b
