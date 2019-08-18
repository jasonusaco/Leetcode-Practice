#s1+s1走两遍里面就包含了任意旋转的字符，所以只要s2在里面就行
def checkReverseEqual(s1,s2):
    return len(s1) == len(s2) and s2 in (s1 + s1)
