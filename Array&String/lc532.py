class Solution:
    def findPairs(self, nums, k):
        #计数器
        count = 0
        #弄一个set把原列表去重
        list_nums = set(nums)
        #如果k等于0，就把
        if k == 0:
            for each in list_nums:
                if nums.count(each) > 1:
                    count += 1
            return count
        elif k < 0:
            return 0
        elif k > 0:
            for i in list_nums:
                if i+k in list_nums:
                    count += 1
        return count
