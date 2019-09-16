class Solution:
    def findWords(self, words):
        row1 = 'qwertyuiopQWERTYUIOP'
        row2 = 'asdfghjklASDFGHJKL'
        row3 = 'zxcvbnmZXCVBNM'
        #用字典来保存字符串在哪一行
        rowdict = {}
        res = []
        #遍历字符串，看他所有的字符在哪几行
        for char in row1:
            rowdict[char] = 1
        for char in row2:
            rowdict[char] = 2
        for char in row3:
            rowdict[char] = 3
            
        for word in words:
            #然后遍历words，用set对行数去重
            #如果set结果等于1，说明就是一行就能拼出来
            if len(set(rowdict[char] for char in word)) == 1:
                res.append(word)
        return res
            
        
