from typing import *
from collections import defaultdict

# time complexity: O(N*N + NlogN)
# space complexity: O(N) 

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp = [1]*N
        preIndex = [-1]*N
        maxi = 0
        for i in range(1,N):
            maxSubset = 1
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] ==0:
                    if dp[j] +1 > maxSubset:
                        maxSubset = dp[j]+1
                        preIndex[i] = j
            if maxSubset > dp[maxi]:
                maxi = i
            dp[i] = maxSubset
        
        ret = []
        index = maxi
        while index>=0:
            ret.append(nums[index])
            index = preIndex[index]
        
        return ret

s = Solution()
# print(s.largestDivisibleSubset(nums = [1,2,4,8]))
print(s.largestDivisibleSubset(nums = [5,9,18,54,108,540,90,180,360,720]))