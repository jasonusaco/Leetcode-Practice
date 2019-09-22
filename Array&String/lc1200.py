class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        #先排序
        arr.sort()
        #建立列表来保存答案
        ans = list()
        #确定最大值
        min_abs = 10**9
        for i in range(len(arr) - 1):
            #遍历过程中，相邻的进行减法计算然后和min_abs比较
            if arr[i + 1] - arr[i] < min_abs:
                #如果小于的话就把值赋给min_abs
                min_abs = arr[i + 1] - arr[i]
                #然后把两个值合成一个list在赋给ans
                ans = [[arr[i], arr[i + 1]]]
            #如果和min_abs相等
            elif arr[i + 1] - arr[i] == min_abs:
                #直接加入到开始建的list里面
                ans.append([arr[i], arr[i + 1]])
        return ans
