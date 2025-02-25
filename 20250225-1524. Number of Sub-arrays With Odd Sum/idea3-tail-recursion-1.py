from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        def helper(index, totalOdd=0, nEven=0, nOdd=0) -> int:
            if(index == len(arr)):
                return totalOdd
            val = arr[-1-index]            
            if val%2 ==0:
                return helper(index+1, (totalOdd+nOdd)% int(1e9+7), nEven+1, nOdd)
            else:          
                return helper(index+1, (totalOdd+nEven + 1)% int(1e9+7), nOdd, nEven+1)
        return helper(0)
            
s = Solution()
print(s.numOfSubarrays([1,3,5]))