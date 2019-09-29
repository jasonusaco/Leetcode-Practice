class Solution:
    def largeGroupPositions(self, S):
        res = []
        i = 0
        while i < len(S):
            j = i
            letter = S[i]
            while j+1 < len(S) and S[j+1] == letter:
                j += 1
            if j-i >= 2:
                res.append([i,j])
            i = j+1
        return res
