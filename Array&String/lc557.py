class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split(' ')
        res = ''
        for i in a:
            i = i[::-1]
            res += i+' '
        return res[:-1]
