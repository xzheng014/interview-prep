class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        heap = nums[:k]
        heapify(heap)

        for n in nums[k:]:
            heappushpop(heap, n)

        return heap[0]