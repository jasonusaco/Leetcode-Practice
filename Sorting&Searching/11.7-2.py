class Stack:
    def getHeight(self, actors, n):
        #记录以i结尾的最长子序列
        k = [0] * n
        #对身高排序
        A = sorted(actors)
        for i in range(n):
            t = 0
            for j in range(i - 1, -1, -1):
                #找最长子序列
                if A[i][1] > A[j][1] and k[j] > t:
                    t = k[j]
            k[i] = t + 1
        return max(k)
