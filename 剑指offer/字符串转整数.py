#逐个判断，最后相加，注意特殊情况
class Solution:
    def StrToInt(self, s):
        numstrs=['0','1','2','3','4','5','6','7','8','9']
        sum = 0
        label = 1
        for i in range(len(s)):
            if i == 0:
                if s[i] == '-':
                    label = -1
                    continue
                elif s[i] == '+':
                    continue
            if s[i] in numstrs:
                sum = sum*10+numstrs.index(s[i])

            else:
                sum = 0
                break
        return sum*label
        
                       
