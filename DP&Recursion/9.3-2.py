"""
跟上题一样，仍然可以直接暴力解
"""
class MagicIndex:
    def findMagicIndex(self, A, n):
        if not A:
            return False
        for i in range(len(A)):
            if A[i] == i:
                return True
            else:
                return False

"""
二分法
"""
class MagicIndex:
    def findMagicIndex(self, A, n):
        if n == 0:
            return True
        return self.magic(A,0,n-1):
    def magic(self, A, start, end):
        if start > end:
            return False
        mid = (start+end)/2
        if mid == A[mid]:
            return True
        else:
            min_v = min(mid-1,A[mid])
            max_v = max(mid+1, A[mid]
            return self.magic(A, start, min_v) or self.magic(A, max_v, end)
