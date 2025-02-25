from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        def helper(i, totalOdd=0, nEven=0, nOdd=0) -> int:
            if(i == -1):
                return totalOdd
            val = arr[i]            
            if val%2 ==0:
                return helper(i-1, (totalOdd+nOdd)% int(1e9+7), nEven+1, nOdd)
            else:          
                return helper(i-1, (totalOdd+nEven + 1)% int(1e9+7), nOdd, nEven+1)
        return helper(len(arr)-1)
            
s = Solution()
print(s.numOfSubarrays([1,3,5]))