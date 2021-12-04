class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """search space: [0, len(nums)) -> target could be larger than the last element"""
        """condition: nums[mid] >= target -> we are looking for the minimum pos that satisfy this condition"""
        """return: left -> minimum pos that satisfies condition will be the pos we insert new element"""

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left