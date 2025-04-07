from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum1=sum(nums)
        if sum1&1: return False
        K=sum1//2
        dp=(1<<K)
        for x in nums:
            dp|=(dp>>x)
            if dp&1: return True
        return dp&1==1
    
    
s = Solution()
# print(s.canPartition([1,5,11,5]))
# print(s.canPartition([3,3,3,4,5]))
# print(s.canPartition([1,2,3,4,5,6,7]))
print(s.canPartition([1,2,5]))