#直接用replace方法
def replaceSpace(iniString, length):
    return iniString.replace(" ","%20")

#建一个list来操作，遍历字符串，遇到空格就append
def replaceSpace(iniString, length):
    l = list()
    i = 0
    while i < length:
        if iniString[i] ==' ':
            l.append('%20')
        else:
            l.append(iniString[i])
        i += 1
    newstr = ''.join(l)
    return newstr
