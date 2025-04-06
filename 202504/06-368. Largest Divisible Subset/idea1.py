from typing import *
from collections import defaultdict

# time complexity: O(N*N + NlogN)
# space complexity: O(N) 

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)
        nums.sort()
        dp = [1]*N
        for i in range(1,N):
            maxSubset = 1
            for j in range(i-1, -1, -1):
                if nums[i]%nums[j] ==0:
                    maxSubset = max(maxSubset, dp[j]+1)
            dp[i] = maxSubset
        
        dpdict = defaultdict(list)
        for i, d in enumerate(dp):
            dpdict[d].append(i)
        ret = []
        maxd = max(dpdict.keys())
        ret.append(nums[dpdict[maxd][0]])
        for d in range(maxd-1, -1, -1):
            for i in dpdict[d]:
                if ret[-1]% nums[i] == 0:
                    ret.append(nums[i])
                    break        
        return ret

s = Solution()
# print(s.largestDivisibleSubset(nums = [1,2,4,8]))
print(s.largestDivisibleSubset(nums = [5,9,18,54,108,540,90,180,360,720]))