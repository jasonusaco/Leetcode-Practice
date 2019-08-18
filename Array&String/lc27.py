#用一个res来记录，如果当前index不等于val
#那么就把这个值赋到res，res+1
#最后返回res即可
def removeElement(nums, val):
    res = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[res] = nums[i]
            res += 1
    return res
