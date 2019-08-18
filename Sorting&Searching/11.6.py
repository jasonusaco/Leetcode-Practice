"""
由于行和列都是递增关系，所以我们可以从最后一行开始
若最后一行的第一个元素小于目标值，则进行列的增加知道相等
若大于目标值，则减小行，再进行判断
"""
class Finder:
    def findElement(self, mat, n, m, x):
        #第一个元素
        i = 0
        #最后一行
        j = m-1
        while not(i >= n or j < 0):
            #k代表最后一行第一个元素
            k = mat[i][j]
            #目标值大于最后一行第一个元素
            #递减
            if x < k:
                j -= 1
                #目标值小于第一个元素，递增
            elif x > k:
                i += 1
            else:
                return [i,j]
