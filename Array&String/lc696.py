class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        N = len(s)
        curlen = 1
        res = []
        for i in range(1, N):
            if s[i] == s[i - 1]:
                curlen += 1
            else:
                res.append(curlen)
                curlen = 1
        res.append(curlen)
        return sum(min(x, y) for x, y in zip(res[:-1], res[1:]))
