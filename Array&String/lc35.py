#这题由于是排好序的列表，直接二分法，注意的是最后return left
def searchInsert(nums,target):
        left = 0 
        right = len(nums) - 1
        
        while left <= right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left
