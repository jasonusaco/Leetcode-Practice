class Solution:
    def isSubtree(self, s, t):
        def isSame(r1, r2):
            if r1 and r2:
                #递归比较
                return r1.val == r2.val and isSame(r1.left, r2.eft) and isSame(r1.right, r2.right)
            return r1 == r2
        if not t:
            return True
        elif not s:
            return False
        return isSame(s,t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
                
        
