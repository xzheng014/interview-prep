class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        """search space: 1, max(bloomDay)"""
        """condition: canMakeBouquet"""
        """return: left"""

        def canMakeBouquet(day):
            flowerCount = 0
            numBouquet = 0

            for bloom in bloomDay:
                if bloom > day:
                    flowerCount = 0
                else:
                    flowerCount += 1
                    if flowerCount == k:
                        numBouquet += 1
                        flowerCount = 0

            return numBouquet >= m

        if m * k > len(bloomDay):
            return -1

        left, right = 1, max(bloomDay)

        while left < right:
            mid = left + (right - left) // 2
            if canMakeBouquet(mid):
                right = mid
            else:
                left = mid + 1

        return left
