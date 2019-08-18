"""
建立一个临时栈用于存放排好序的栈，然后在建一个临时变量来存放
即将弹出的栈顶，把新栈里面比临时变量大的数弹回原栈
然后把临时变量加入到新栈中，日此往复
最后返回新栈
"""
class TwoStacks:
    def twoStacksSort(self, numbers):
        #如果是空栈的话就返回空
        if not numbers:
            return []

        result = []

        while numbers:
            #临时变量用于存放原栈的栈顶
            temp = numbers.pop()
            #把比temp大的数弹回到原栈
            while result and result[-1] < temp:
                numbers.append(result.pop())
            #再把temp加入到临时栈
            result.append(temp)
        #返回最后临时栈的结果
        return result
        
