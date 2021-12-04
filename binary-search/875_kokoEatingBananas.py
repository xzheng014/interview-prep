class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        """search space: [1, max(piles)]"""
        """condition: canEat"""
        """return: left"""

        def canEat(speed):
            hours = 0
            for pile in piles:
                hours += pile // speed
                if pile % speed:
                    hours += 1
                if hours > h:
                    return False
            return True

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2
            if canEat(mid):
                right = mid
            else:
                left = mid + 1

        return left
