"""

时间复杂度O(N),按书中所讲，3个素数因子3、5、7分为三个队列
q3,q5,q7，其中最初存放3，5，7
     * 之后每次添加找到三个队列头中最小的数，起初为3，将3移出队列
q3后，在q3添加3*3，在q5添加3*5,q7中添加3*7
     * 此时可知q3{3*3},q5{5,3*5},q7{7,3*7}
     * 下一轮找到最小数为5，重复上述步骤，将5从q5移出，添加5*5到
q5，因为5*3已经添加过所以不需要添加到q3中
     * 将5*7添加到q7，结果q3{3*3},q5{3*5,5*5},q7{7,3*7,5*7}
     * 依次找到第k个数
"""

class KthNumber:
    def findKth(self, k):

        queue3 = [3]
        queue5 = [5]
        queue7 = [7]
        count = 0

        while count < k:
            min_s = min(queue3[0], queue5[0], queue7[0])
            if min_s == queue3[0]:
                min_s = queue3.pop(0)
                queue3.append(min_s*3)
                queue5.append(min_s*5)
            elif min_s == queue5[0]:
                min_s = queue5.pop(0)
                queue5.append(min_s*5)
            else:
                min_s == queue7[0]
                min_s = queue7.pop(0)
            queue7.append(min_s*7)
            count += 1
        return min_s
