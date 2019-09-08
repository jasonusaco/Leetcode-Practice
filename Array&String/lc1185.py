"""
直接用方法
"""
import time
import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.datetime(year, month, day).strftime("%A")
