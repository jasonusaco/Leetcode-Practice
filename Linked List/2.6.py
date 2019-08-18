#建一个列表，扫一遍链表，把元素逐个存入列表
#然后直接list[::-1]和原来的列表对比即可
def isPalindrome(pHead):
    arr = []
    while pHead:
        arr.append(pHead.val)
        pHead = pHead.next
    return arr == arr[::-1]
