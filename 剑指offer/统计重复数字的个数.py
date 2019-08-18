class Solution:
    def duplicate(self, numbers, duplication):
        #去重
        numset = set(numbers)
        dict = {}
        duplication.append(0)
        for val in numbers:
            dict[val] = 0
        for i in range(0, len(numbers)):
            dict[numbers[i]] = dict[numbers[i]]+1
        for val in numset:
            if dict[val] > 1:
                dupication[0] = val
                return True
        return False
        
