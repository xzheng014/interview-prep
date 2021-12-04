class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l, r = 0, 0
        minStart = -1
        minLength = float('inf')
        map_ = [0]*128
        count = len(t)
        
        for c in t:
            map_[ord(c)] += 1
        
        while r < len(s):
            if map_[ord(s[r])] > 0:
                count -= 1
            map_[ord(s[r])] -= 1
            r += 1
            
            while count == 0:
                if minLength > r - l:
                    minLength = r - l
                    minStart = l
                map_[ord(s[l])] += 1
                if map_[ord(s[l])] > 0:
                    count += 1
                l += 1
        
        if minStart == -1: 
            return ""
        
        return s[minStart:minStart + minLength]
