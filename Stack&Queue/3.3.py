class SetOfStacks:
    def setOfStacks(self, ope, size):
        if not ope:
            return []
        #创建一个二维数组
        result = [[]]
        for op in ope:
            if op[0] == 1:
                if len(result[-1]) == size:
                    result.append([])
                result[-1].append(op[1])
            else:
                if len(result[-1]) == 0:
                    result.pop()
                result[-1].pop()
        return result
