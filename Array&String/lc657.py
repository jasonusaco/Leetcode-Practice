"""
就是看上和下移动步数和左右移动步数是否相等
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = d = l = r = 0
        for move in moves:
            if move == 'U':
                u += 1
            elif move == "D":
                d += 1
            elif move == 'L':
                l += 1
            elif move == 'R':
                r += 1
        return u == d and l == r

"""
用Counter会更简洁
"""
from collections import Counter
class Solution:
    def judgeCircle(self, moves):
        count = collections.Counter(moves)
        return count['U'] == count['D'] and count['L'] == count['R']
