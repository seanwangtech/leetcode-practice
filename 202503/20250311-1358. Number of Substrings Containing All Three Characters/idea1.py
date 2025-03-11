# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        chrFreq = {}
        iLow = -1
        count = 0
        for chr in s:
            chrFreq[chr] = chrFreq.get(chr, 0) +1
            if len(chrFreq) == 3:
                if iLow == -1:
                    iLow = 0
                while chrFreq[s[iLow]] > 1:
                    chrFreq[s[iLow]] -= 1
                    iLow += 1
            count += iLow +1 
        return count
    
s = Solution()
print(s.numberOfSubstrings("abcabc"))