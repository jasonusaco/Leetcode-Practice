class Solution:
    def calPoints(self, ops):
        #构建列表储存有效数字
        res = []
        #遍历ops，当op为数字时，将op转化为int存入res
        for op in ops:
            if op.isdigit() or (op[0] == '-' and len(op) > 1):
                res.append(int(op))
            elif op == '+':
                res.append(res[-1] + res[-2])
            elif op == 'D':
                res.append(2*res[-1])
            elif op == 'C':
                res.pop()
        return sum(res)
