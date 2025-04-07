from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total%2 != 0:
            return False
        else:
            half = total//2
        dp = [0]*(half+1)
        for i in range(1, N):
            num = nums[i-1]
            if num > half:
                return False
            for j in range(half, 0,-1):
                if num<=j:
                    dp[j] = max(
                        dp[j],
                        dp[j-num]+num
                    )
            if dp[-1] == half:
                return True
        return False
                    
    
    
s = Solution()
# print(s.canPartition([1,5,11,5]))
# print(s.canPartition([3,3,3,4,5]))
print(s.canPartition([1,2,3,4,5,6,7]))