class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        """search space: [0, x + 1) -> x to cover cases 0 and 1"""
        """condition: mid * mid > x"""
        """return left - 1"""

        left, right = 0, x + 1

        while left < right:
            mid = left + (right - left)//2
            if mid * mid > x:
                right = mid
            else:
                left = mid + 1

        return left - 1