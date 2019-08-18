#暴力解法，依次从字符串的每个位置开始，
#截取和子字符串相同长度的字符串，与给定的子字符串进行比较。
def strStr(haystack, neddle):
    for i in range(len(haystack)-len(neddle)+1):
        if haystack[i:i+len(neddle)] == neddle:
            return i
    return -1

#Python的find方法
def strStr(haystack, neddle):
    return haystack.find(needle)
