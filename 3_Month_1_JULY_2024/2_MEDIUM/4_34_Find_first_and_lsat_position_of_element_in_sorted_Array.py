# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
# Medium

class Solution(object):
    def searchRange(self, nums, target):
        def first(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < len(nums) and nums[left] == target else -1
                    
        def last(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return right if right >= 0 and nums[right] == target else -1


        return first(nums, target), last(nums, target)