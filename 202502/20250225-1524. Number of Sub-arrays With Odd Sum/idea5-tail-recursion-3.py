from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        def helper(arr,index=0, totalOdd=0, nEven=0, nOdd=0) -> int:
            i = len(arr)-1-index
            if(i == -1):
                return totalOdd
            val = arr[i]
            if val%2 ==0:
                return helper(arr,index+1, (totalOdd+nOdd)% int(1e9+7), nEven+1, nOdd)
            else:          
                return helper(arr,index+1, (totalOdd+nEven + 1)% int(1e9+7), nOdd, nEven+1)
        return helper(arr)
            
s = Solution()
print(s.numOfSubarrays([1,3,5]))