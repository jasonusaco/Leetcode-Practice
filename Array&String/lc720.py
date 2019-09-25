class Solution:
    def longestWord(self, words):
        if not words:
            return ""
        longestword = ''
        wordset = set([''])
        #按照字母顺序排列
        words.sort()
        #遍历words
        for word in words:
            #如果当前word除了最后一个字母以外的字符串在set中
            if word[:-1] in wordset:
                #则把word加入到set中
                wordset.add(word)
                #然后把当前word和最长word比较
                if len(longestword) < len(word):
                    longestword = word
        return longestword
