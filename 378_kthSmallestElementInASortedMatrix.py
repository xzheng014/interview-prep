class Solution(object):
    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []

        for row in matrix:
            for element in row:
                heappush(heap, 0 - element)
                if len(heap) > k:
                    heappop(heap)

        return 0 - heappop(heap)


class Solution(object):
    def kthSmallest2(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        heap = []

        for i in range(min(len(matrix), k)):
            heappush(heap, (matrix[i][0], i, 0))

        ans = -1
        i = 0

        while i < k:
            ans, r, c = heappop(heap)
            if c + 1 < len(matrix[0]):
                heappush(heap, (matrix[r][c + 1], r, c + 1))
            i += 1

        return ans


class Solution(object):
    def kthSmallest3(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix: return -1

        left, right = matrix[0][0], matrix[-1][-1]

        def smallerElementinMatrix(val):
            r = 0
            count = 0
            while r < len(matrix):
                c = len(matrix[0]) - 1
                while c >= 0:
                    if matrix[r][c] <= val:
                        count += (c + 1)
                        break
                    c -= 1
                r += 1
            return count

        while left < right:
            mid = left + (right - left) // 2
            if smallerElementinMatrix(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left
