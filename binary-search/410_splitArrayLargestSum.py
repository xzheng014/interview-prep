class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        """search space: left = sum(nums)/m, right = sum(nums)"""
        """condition: isFeasible(mid)"""
        """return: left"""

        def isFeasible(largest_sum):
            target = 0
            m_counter = 1
            for num in nums:
                target += num
                if target > largest_sum:
                    target = num
                    m_counter += 1
                if m_counter > m:
                    return False
            return True

        left, right = max(nums), sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if isFeasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
