"""
方法1：题目中明确说了t很长，所以要尽量只对t遍历一次，
可以用一个队列保留s的每个元素，然后对t进行遍历
如果遍历到的元素和队列的头元素相等，那么队列出头元素
最后返回队列是否为空即可
"""
class Solution(object):
    def isSubsequence(self, s, t):
        #建立队列
        queue = collections.deque(s)
        #遍历长字符串
        for c in t:
            if not queue:
                return True
            #遍历到和队列头相等则弹出
            if c == queue[0]:
                queue.popleft()
        #判断剩下的队列是否为空
        return not queue

"""
方法2：双指针法，一个为s的索引，一个为t的索引，如果在t中找到了s的元素，把s的指针向右移
否则把t的指针右移,最后检测索引的数量和s的长度是否相等
"""
class Solution(object):
    def isSubsequene(self, s, t):
        si = 0
        ti = 0
        while si < len(s) and ti < len(t):
            if t[ti] == s[si]:
                si += 1
            ti += 1
        return si == len(s)
        
