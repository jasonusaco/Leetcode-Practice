#用到别的数据结构
def checkDifferent(iniString):
    a = set(iniString)
    if len(a) == len(iniString):
        return True
    else:
        return False

#不用别的数据结构
def checkDifferent(iniString):
    for i in range(len(iniString):
        for j in range(i+1, len(iniString)):
            if iniString[i] == iniString[j]:
                return False
    return True
                
