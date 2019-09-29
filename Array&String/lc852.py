"""
二叉搜索，跟传统的二分法区别在于，不是比较left，right，mid三者关系
而是比较mid与相邻的两个元素的关系，根据是否符合山峰上坡和下坡去移动指针
"""
class Solution:
    def peakIndexInMountainArray(self, A):
        left = 0
        right = len(A)
        while left < right:
            mid = left +(right-left) // 2
            if A[mid-1] < A[mid] and A[mid] > A[mid+1]:
                return mid
            if A[mid] < A[mid+1]:
                left = mid + 1
            else:
                right = mid
        return -1
