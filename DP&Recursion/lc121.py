"""
思路1：我们可以把价格数组看成涨跌数组，这样就
相当于转化成了一个最大子数组求和的问题
比如给定价格数组为[7,1,5,3,6,4]
涨跌数组就是[-6,4,-2,3,-2]，会少一个元素，因为第一个数无涨跌
这里涨跌数组的最大连续子数组之和便是我们能赚到的最大利润
"""
class Solution(object):
    def maxProfit(self, prices):
        size = len(prices)
        #小于等于1的话木有卖所以没利润
        if size <= 1:
            return 0
        lastMax = prices[1] - prices[0]
        res = max(0,lastMax)
        for i in range(1, size -1):
            profit = prices[i+1] - prices[i]
            if lastMax <= 0:
                lastMax = profit
            else:
                lastMax += profit
            res = max(lastMax, res)

"""
思路2:记录当前最小值min，遍历的时候如果array[i]小于min，就更新min
否则计算如果在第i天卖的利润和当前最大利润比较
即最小值与最新遍历点的差值，最大的即为最大交易
"""
class Solution(object):
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        result = 0
        mins = prices[0]
        for i in prices:
            if i > mins:
                #result就是当前最大利润，
                #i-mins就是当天卖的利润
                #两个对比取大的就是最大利润了
                result = max(result, i-mins)
            else:
                mins = i
        return result
        
