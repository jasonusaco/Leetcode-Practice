
class Solution:
    def InversePairs(self, data):
        #特殊情况
        if len(data) <= 0:
            return 0
        count = 0
        copy = []
        #在data中遍历，把每一个值加入到copy中
        for i in range(len(data)):
            copy.append(data[i])
        #对copy排序
        copy.sort()
        i = 0
        while len(copy) > i:
            #把data中每一个对应的copy元素的index加入到count中
            count += data.index(copy[i])
            #加入一个就移出一个
            data.remove(copy[i])
            #每移除一个i就+1以终止遍历
            i += 1
        return count%1000000007
            
                    
