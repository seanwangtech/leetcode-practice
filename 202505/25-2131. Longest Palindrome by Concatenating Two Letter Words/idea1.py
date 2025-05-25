from collections import defaultdict
from typing import *

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        N = len(words)
        freqab = defaultdict(lambda:[0,0])
        freqaa = defaultdict(int)
        for c0,c1 in words:
            if c0 == c1:
                freqaa[ord(c0)] += 1
            else:
                if c0 < c1:
                    freqab[ord(c0)+ord(c1)*128][0] += 1
                else:
                    freqab[ord(c1)+ord(c0)*128][1] += 1
        count = 0
        for f1,f2 in freqab.values():
            count += 4*min(f1,f2)
        hasOddf = False
        for f in freqaa.values():
            count += 4* (f//2)
            if (f%2 == 1):
                hasOddf = True
        if hasOddf:
            count += 2
        return count
        
        
        
s = Solution()
print(s.longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))