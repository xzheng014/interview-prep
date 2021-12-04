class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        """search space: left - max(weights), right - sum(weights)"""
        """condition: ableToship -> define a function"""
        """return left -> smallest val that satisfies the condition"""

        left, right = max(weights), sum(weights)

        def ableToShip(capacity):
            countOfDays = 1
            target = 0
            for weight in weights:
                target += weight
                if target > capacity:
                    countOfDays += 1
                    target = weight
                if countOfDays > days:
                    return False
            return True

        while left < right:
            mid = left + (right - left)//2
            if ableToShip(mid):
                right = mid
            else:
                left = mid + 1

        return left
