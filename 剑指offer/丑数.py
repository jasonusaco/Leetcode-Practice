"""
按顺序把每个丑数放在数组中，求下一个丑数
下一个丑数必定由数组中某一个丑数A*2, b*3, c*5中最小值得来
在数组中必定有一个丑数M2，在他之前的数*2都小于当前最大丑数
在他之后的数*2都大于当前最大丑数
"""
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index < 1:
            return 0
        res = [1]
        t2 = t3 = t5 = 0

        nextIdx = 1
        while nextIdx < index:
            minNum = min(res[t2] * 2, res[t3] * 3, res[t5] * 5)
            res.append(minNum)

            while res[t2]*2 <= minNum:
                t2 += 1
            while res[t3]*3 <= minNum:
                t3 += 1
            while res[t5]*5 <= minNum:
                t5 += 1
            nextIdx += 1
        return res[nextIdx-1]
