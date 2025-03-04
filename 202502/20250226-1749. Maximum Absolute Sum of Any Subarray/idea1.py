from typing import *
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxabsSum = 0
        imin = 0 # minimum sum value for subarrays end with index i
        imax = 0 # maximum sum value for subarrays end with index i
        for val in nums:
            imin = imin + val if imin<0 else val
            imax = imax + val if imax>0 else val
            maxabsSum = max(maxabsSum, abs(imin), abs(imax))
        return maxabsSum
    
    
s = Solution()
print(s.maxAbsoluteSum(nums = [1,-3,2,3,-4]))