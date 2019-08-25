class Solution:
    def combinationSum(self, candidates, target):
        #下面有一个目标值小于某一元素就break，所以先排序
        candidates.sort()
        #储存返回的二维列表
        res = []
        length = len(candidates)
        #递归，目标值，起始位置，当前组合
        def dfs(target, start, vlist):
            #目标值为0，表明当前递归完成，把当前结果加入res并返回
            if target == 0:
                return res.append(vlist)
            #从开始下标循环
            for i in range(start, length):
                #candidates有序，只要当前大于目标后面都大于，直接break
                if target < candidates[i]:
                    break
                #加个判定条件保证不重复,遇到重复的直接跳过
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                #否则目标值减当前值，i为新的起始位置，把当前值加入当前组合
                else:
                    dfs(target - candidates[i], i+1, vlist + [candidates[i]])
        dfs(target, 0, [])
        return res
