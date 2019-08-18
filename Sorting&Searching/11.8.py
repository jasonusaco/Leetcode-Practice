def getRankOfNumber(self, A, n):
    #用于存放要返回的列表
    newList = [0]
    for i in range(1,n):
        num = 0
        #每次遍历就看是否有比他小的数，计算出数量
        for j in range(0, i):
            if A[j] <= A[i]:
                num += 1
        newList.append(num)
    return newList
