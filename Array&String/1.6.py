#pre记录上个字符，cnt为当前字符计数，循环完在加上压缩串
def zipString(iniString):
    pre = ''
    cnt = 0
    ss = ''
    for s in iniString:
        if s == pre:
            cnt += 1
        else:
            if pre:
                ss += pre + str(cnt)
            pre = s
            cnt = 1
    ss += pre + str(cnt)
    if len(ss) < len(iniString):
        return ss
    else:
        return iniString

#方法2
def zipString(str):
    if len(str) == 0:
        return str

    ans = []
    count = 1
    last = str[0]
    for c in str[1:]:
        if c == last:
            count += 1
        else:
            ans.append(last)
            ans.append("%s" % count)
            last = c
            count = 1

    ans.append(last)
    ans.append("%s" % count)

    if len(ans) < len(str):
        return ''.join(ans)
    else:
        return str
