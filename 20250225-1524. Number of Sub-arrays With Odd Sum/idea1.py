from typing import *


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        self.totalOdd = 0
        def helper( index) -> Tuple[int, int]:
            if(index == len(arr)):
                return (0,0)
            val = arr[index]
            nEven, nOdd = helper(index+1)
            
            if val%2 ==0:
                # even number
                self.totalOdd = (self.totalOdd+nOdd)% int(1e9+7)
                return (nEven+1, nOdd)
            else:
                self.totalOdd = (self.totalOdd+nEven + 1)% int(1e9+7)
                return (nOdd, nEven+1)
        helper(0)
        return self.totalOdd
            
s = Solution()
print(s.numOfSubarrays([1,3,5]))