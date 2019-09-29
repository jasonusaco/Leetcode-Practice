"""
遇到#，字符串不为空，就删除最后一个字符。如果不是#号，
就拼接到字符串的最后。把两个字符串都求出来，然后比较就好。
"""

class Solution(object):
    def backspaceCompare(self, S, T):
        ans_T = ''
        ans_S = ''
        for s in S:
            if s == '#':
                if ans_S:
                    ans_S = ans_S[:-1]
            else:
                ans_S += s
        for t in T:
            if t == '#':
                if ans_T:
                    ans_T = ans_T[:-1]
            else:
                ans_T += t
        return ans_S == ans_T
        
