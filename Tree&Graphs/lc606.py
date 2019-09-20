class Solution:
    def tree2str(self, t):
        if not t:
            return ''
        res = ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left or right:
            res += '(%s)' % left
        if right:
            res += '(%s)' % right
        return str(t.val) +res
