class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left, right = 0, 0
        hashMap = [0]*128
        count = 0
        maxLength = 0
        
        while right < len(s):
            if hashMap[ord(s[right])] > 0:
                count += 1
            hashMap[ord(s[right])] += 1
            right += 1
            
            while count > 0:
                if hashMap[ord(s[left])] > 1:
                    count -= 1
                hashMap[ord(s[left])] -= 1
                left += 1
            
            maxLength = max(maxLength, right - left)
        
        return maxLength
