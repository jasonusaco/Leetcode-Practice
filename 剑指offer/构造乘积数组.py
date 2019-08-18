class Solution:
    def multiply(self, A):
        if not A:
            return []
        B = [1] * len(A)
        #从上往下累乘左下半
        for i in range(1, len(A)):
            B[i] = B[i-1] * A[i-1]
        #从下往上累乘右上半
        temp = 1
        for i in range(len(A)-2, -1,-1):
            temp *= A[i+1]
            B[i] *= temp
        return B
