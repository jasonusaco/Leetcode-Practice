"""
用stack和字典来做
"""
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        #建立字典
        d = {}
        #建立栈
        stack = []
        #储存答案
        ans = []
        #遍历列表2，如果此时栈不为空，
        #切栈顶元素stack[-1]小于当前数字，则说明当前数字就是栈顶元素的右边第一个较大数
        for i in nums2:
            while len(stack) and  stack[-1] < i:
                #那么就建立映射关系，并除去栈顶的元素
                d[stack.pop()] = i
            #最后将当前遍历到的数字压入栈
            stack.append(i)
        for j in nums1:
            #使用字典的get方法获取，如果没有的话就默认返回-1
            ans.append(d.get(j,-1))
        return ans
        
        
