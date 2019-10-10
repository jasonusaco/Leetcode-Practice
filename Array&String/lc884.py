from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        a_arr = A.split(' ')
        b_arr = B.split(' ')
        arr = a_arr+b_arr
        cnt = Counter(arr)
        res = []
        for i in arr:
            if cnt[i] == 1:
                res.append(i)
        return res
