from typing import *
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1000_000_007
        freq = [0]*26
        for chr in s:
            freq[ord(chr)-ord('a')] += 1
        for _ in range(t):
            tnums2 = [0]*26
            for i in range(26):
                for j in range(1, nums[i]+1):
                    tnums2[(i+j)%26] += freq[i]%MOD
            freq = tnums2
            print(freq)
        return sum(freq)%MOD
    
s = Solution()
print(s.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))