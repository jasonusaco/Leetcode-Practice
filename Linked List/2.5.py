"""
先把a和b表示的整数取出来，在计算两个数的和，最后把和表示为链表
"""

def plusAB(a,b):
    resA = []
    resB = []

    #把a和b的值分别以字符串的形式取出来装在新list里面
    #每取一个就.next往前进一个
    while a:
        resA.append(str(a.val))
        a = a.next
    while b:
        resB.append(str(b.val))
        b = b.next

    #计算a+b的和
    result = str(int("".join(resA[::-1])) + int("".join(resB[::-1])))

    #创建一个链表，从个位开始存放
    dummy = ListNode(0)
    pre = dummy
    for i in result[::-1]:
        node = ListNode(int(i))
        pre.next = node
        pre = pre.next
    return dummy.next
        
    
