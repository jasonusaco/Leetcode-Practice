class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        nums = sorted(set(letters))
        if target < nums[0]:
            return nums[0]
        if target == nums[0]:
            return nums[1]
        if target >= nums[-1]:
            return nums[0]
        if target > nums[0] and target < nums[-1]:
            letters.append(target)
            nums = sorted(set(letters))
            return nums[nums.index(target)+1]

"""
二分法
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if letters[middle] <= target:
                left = middle + 1
            else:
                right = middle - 1
        if left < len(letters):
            return letters[left]
        else:
            return letters[0]
