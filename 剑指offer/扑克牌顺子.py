"""
如果输入为空，直接返回false，
除了王以外，任何数值的牌只要出现2个或者更多，一定凑不齐顺子
先统计王的数量，再把牌排序，如果后面一个数
比前面一个数大于1以上，那么中间的差值就必须用王来补了，看王
的数量够不够，如果够就返回true，否则false
"""
class Solution:
    def IsContinuous(self, numbers):
        if len(numbers) < 5:
            return False
        #王的数量
        nOfZero = numbers.count(0)
        numbers.sort()
        #序列中间隔的值初始化为0
        sumOfGap = 0
        #遍历非0部分的递增序列
        for i in range(nOfZero, len(numbers)-1):
            #当前值与下一个值的比较，若相等则说明存在对子
            if numbers[i] == numbers[i+1]:
                return False
            else:
                #如果不同，则二者的查再减1，如果为0说明连续
                #不为0则之间存在空
                sumOfGap += (numbers[i+1] - numbers[i] - 1)
        #看王的数量够不够补差值，够的话返回True
        if nOfZero >= sumOfGap:
            return True
        else:
            return False
            
        
