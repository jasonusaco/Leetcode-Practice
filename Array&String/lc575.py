"""
如果糖果的种类够N//2种，那么可以给其中一堆N//2种，否则最多只能给糖果种类数个不同种类的谈过。
"""
class Solution:
    def distributeCandies(self, candies):
        return min(len(set(candies)), len(candies)//2)
