from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        totalOdd = 0
        nOdd = 0
        nEven = 0
        for index in range(len(arr)):
            i = len(arr)-index-1
            val = arr[i]
            if(val%2 ==0):
                nEven = nEven+1
            else:
                nEven,nOdd = nOdd, nEven+1
            totalOdd = (totalOdd + nOdd)% int(1e9+7)
                
        return totalOdd
            
s = Solution()
print(s.numOfSubarrays([1,3,5]))