#用set方法，两个set如果相等就说明每次单词都是一样的
def checkSam(stringA, stringB):
    return set(stringA) == set(stringB)

#也可以统计字符出现频率，然后对比
from collections import Counter
def checkSam(stringA, stringB):
    return len(stringA) == len(stringB) and Counter(stringA) == Counter(stringB)
