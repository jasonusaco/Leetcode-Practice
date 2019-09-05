"""
反转某个东西，可以用栈，把所有元音字符进栈，再次遍历的时候遇到元音字符就出栈
"""
class Solution:
    def reverseVowels(self, s):
        vstack = []
        for c in s:
            if c in "aeiouAEIOU":
                vstack.append(c)
        res = []
        for c in s:
            if c in "aeiouAEIOUS":
                res.append(vstack.pop())
            else:
                res.append(c)
        return "".join(res)
