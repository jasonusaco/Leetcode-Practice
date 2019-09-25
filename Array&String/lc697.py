"""
使用dict记录每个元素出现的次数，找到出现次数最多的元素，
从开头找到这个元素第一次出现的位置left，再从尾部开始向前找到该元素最后一次
出现位置right，那么最小array的长度就是right-left+1
"""
class Solution:
    def findShortestSubArray(self, nums):
        #定义字典以及对应的位置信息，count记录每个元素的出现次数
        left = {}
        right = {}
        count = {}
        for i, num in enumerate(nums):
            #如果元素num第一次出现，则存入left中
            if num not in left:
                left[num] = i
            #将出现的元素及对应的位置信息存入right中
            right[num] = i
            #每个元素出现一次，则count对应num位置的数值+1
            count[num] = count.get(num, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for num in count:
            if count[num] == degree:
                ans = min(ans, right[num]-left[num]+1)
        return ans
