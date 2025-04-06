from typing import *

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        ors = 0
        for num in nums:
            ors |= num
        return ors<<(N-1)
s = Solution()
print(s.subsetXORSum(nums = [1,3]))
print(s.subsetXORSum(nums = [5,1,6]))