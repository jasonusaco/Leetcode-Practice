class Solution:
    def uniqueMorseRepresentations(self, words):
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        #存入字典，对应的字母和对应的摩斯码
        dic = dict(zip(letter, morse))
        res = set()
        #遍历给的每一个词
        for word in words:
            mword = ''
            #遍历每一个词的每个字母
            for w in word:
                #抽取对应字典中的摩斯码加起来
                mword += dic[w]
            res.add(mword)
        return len(res)
