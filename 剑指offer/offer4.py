"""
直接遍历
"""
class Solution:
    def Find(self, target, array):
        for i in array:
            for j in i:
                if j == target:
                    return j
