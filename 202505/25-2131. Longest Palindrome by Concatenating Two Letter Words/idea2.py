from collections import defaultdict
from typing import *

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        N = len(words)
        freq= defaultdict(int)
        for word in words:
            freq[word] += 1
        count = 0
        isCountaaOdd = False
        for w, f in freq.items():
            r = w[::-1]
            if w == r:
                count += (f//2)*4
                if f%2 ==1:
                    isCountaaOdd = True
            elif w < r and r in freq:
                count += min(f, freq[r])*4
                
        return count+2 if isCountaaOdd else count

s = Solution()
print(s.longestPalindrome(words = ["dd","aa","bb","dd","aa","dd","bb","dd","aa","cc","bb","cc","dd","cc"]))