"""
"""
class Permutation:
    def getPermutation(self, A):
        if not A:
            return []
        elif len(A) == 1:
            return [A]
        res = []
        for i,c in enumerate(A):
            for s in self.getPermutation(A[:i]+A[i+1:]):
                res.append(c+s)
        res.sort(reverse=True)
        return res
