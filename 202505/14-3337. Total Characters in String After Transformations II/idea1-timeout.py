from typing import *
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 1000_000_007
        freq = [0]*26
        for chr in s:
            freq[ord(chr)-ord('a')] += 1
        tnums = [1]*26
        for _ in range(t):
            tnums2 = [0]*26
            for i in range(26):
                for j in range(1, nums[i]+1):
                    tnums2[i] += tnums[(i+j)%26]
                tnums2[i] %= MOD
            tnums = tnums2
        count = 0
        for i, f in enumerate(freq):
            count += tnums[i]*f
            count %= MOD
        return count
s = Solution()
print(s.lengthAfterTransformations(s = "abcyy", t = 2, nums = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))