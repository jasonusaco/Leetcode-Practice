#python秒杀法，用split和rstrip方法
#rstrip是删除字符串末尾的指定字符
def lengthOfLastWord(s):
    return len(s.rstrip().split('')[-1])

#从最后一个字符开始搜索，如果非空格，则往前推一位，直到不是空格
#此时开始记录起始位置，然后继续搜索，直到下一个空格或者到了第一个位置
#记为终点，长度则为起始位置减去终点位置
def lengthOfLastWord(s):
    count = 0
    first = len(s)-1
    while first >= 0 and s[first]==' ':
        first -= 1
    while first >= 0 and s[first] != ' ':
        first -= 1
        count += 1
    return count
        
