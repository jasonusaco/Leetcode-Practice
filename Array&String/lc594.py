from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        #统计每个数字出现的次数
        counter = Counter(nums)
        #对源列表去重
        nums_set = set(nums)
        longest = 0
        #遍历去重后的列表
        for num in nums_set:
            #如果num+1在counter里面的话，就保存num和num+1的和
            if num + 1 in counter:
                longest = max(longest, counter[num]+counter[num+1])
        return longest
