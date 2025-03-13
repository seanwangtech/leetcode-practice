#time complexity O(n)
#space complexity O(1)
from typing import *
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        negn = 0
        posn = 0
        for n in nums:
            if(n<0):
                negn += 1
            elif(n>0):
                posn += 1
        return max(negn, posn)
    
s = Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))