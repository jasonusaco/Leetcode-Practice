class Solution:
    def buddyStrings(self, A, B):
        #如果AB长度不相等，一定是false
        if len(A)!=len(B):
            return False
        #如果相等，肯定有重复元素，而且交换的时候交换重复元素才能true
        if A==B and len(A)!=len(set(A)):
            return True
        #如果A和B仅仅是长度相等而本身不相等，那么顺序遍历，
        #若A[i]和B[i]不相等，则记录这对，最后不相等的一定要是两对，而且这两对互为相反。
        dif=[(a,b) for a,b in zip(A,B) if a!=b]
        return len(dif)==2 and dif[0]==dif[1][::-1]
