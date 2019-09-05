"""
先用set()消除 ransomNote 中重复的元素 ，
再用 count() 计算 magazine 中对应元素的个数是否小于 ransomNote 中的个数
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        for i in set(magazine):
            if magazine.count(i) < ransomNote.count(i):
                return False
        return True
