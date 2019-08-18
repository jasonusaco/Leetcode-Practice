"""
初始结果集为[[A[0]]，遍历剩余的A[1]-A[n-1]
每取出一个元素加到结果集
复制一份结果集，并把元素加入到结果集中每个集合的头部
合并复制的结果集+只有当前元素的集合+原始结果集
"""
class Subset:
    def getSubsets(self, A, n):
        #结果集初始化，一开始只有A[0]
        result = [[A[0]]]
        #开始遍历
        for i in range(1, n):
            temp = result[:]
            for j in range(len(temp)):
                temp[j] = [A[i]] + temp[j]
            result = temp + [[A[i]]] + result
        return result
