    def binarySearch1(self, arr, k): # lower_bound,
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r) // 2
            if arr[mid] < k:
                l = mid + 1
            else:
                r = mid
        return l
    
    def binarySearch2(self, arr, k): 
        l, r = 0, len(arr) - 1
        while l < r:
            mid = (l + r + 1) // 2
            if arr[mid] <= k:
                l = mid
            else:
                r = mid - 1
        return l
