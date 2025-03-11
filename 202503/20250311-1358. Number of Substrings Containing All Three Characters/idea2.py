# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        lastPos = [-1]*3
        count = 0
        for i in range(len(s)):
            lastPos[ord(s[i])-ord('a')] = i
            count += 1 + min(lastPos) 
        return count
    
s = Solution()
print(s.numberOfSubstrings("abcabc"))