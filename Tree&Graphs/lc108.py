# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
"""
由于给了有序数组，所以可以想到二分法
然后也要遍历树，所以也要结合递归
选择中间元素为root，左边就是左子树
右边就是右子树
递归重复1,2,3步骤
"""

class Solution(object):
    def sortedArrayToBST(self, nums):
        #如果是空数组的话
        if nums == []:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:index])
        root.right = self.sortedArrayToBST(nums[index+1:])
        return root

    
