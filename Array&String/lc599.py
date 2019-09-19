class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) > len(list2):
            return self.findRestaurant(list2, list1)
        
        d = {s: i for i, s in enumerate(list1)}
        
        minIdxSum = float('inf')
        res = []
        for i, s in enumerate(list2):
            if s in d:
                idxSum = d[s] + i 
                if idxSum < minIdxSum:
                    minIdxSum = idxSum
                    del res[:]
                    res.append(s)
                elif idxSum == minIdxSum:
                    res.append(s)
        return res
