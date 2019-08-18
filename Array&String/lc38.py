"""
本题的一个关键就是要把list转成char，不然无法统计数字出现次数
"""
def countAndSay(n):
    #将第一行的1转换成字符类型，方便下一行读取
    b = '1'
    #在n-1中遍历，因为第一行不需要处理，所以是n-1
    for i in range(n-1):
        #a用于读取上一回的第一个字符
        a = b[0]
        #c用于存放读出的内容，char
        c = ''
        #count用来统计
        count = 0
        for j in b:
            if a == j:
                count += 1
            else:
                c += str(count)+a
                a = j
                count = 1

        c += str(count)+a
        b = c
    return b
