from typing import *

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        # top down
        N = len(nums)
        mem = [[-1]*(k+1) for x in range(N)]
        def helper(index, k):
            if(mem[index][k] != -1):
                return mem[index][k]
            if(k == 1):
                mem[index][k] = min(nums[index:])
                return mem[index][k]
            if(len(nums)-index < 2*k):
                mem[index][k] = max(helper(index+2, k-1), nums[index])
                return mem[index][k]
            mem[index][k] = min(
                max(helper(index+2, k-1), nums[index]), 
                helper(index+1, k)
            )
            return mem[index][k]
            
        return helper(0, k)

s = Solution()
print(s.minCapability([7,3,9,5],2))
print(s.minCapability([5038,3053,2825,3638,4648,3259,4948,4248,4940,2834,109,5224,5097,4708,2162,3438,4152,4134], 6))
print(s.minCapability([5038,3053,2825,3638,4648,3259,4948,4248,4940,2834,109,5224,5097,4708,2162,3438,4152,4134,551,3961,2294,3961,1327,2395,1002,763,4296,3147,5069,2156,572,1261,4272,4158,5186,2543,5055,4735,2325,1206,1019,1257,5048,1563,3507,4269,5328,173,5007,2392,967,2768,86,3401,3667,4406,4487,876,1530,819,1320,883,1101,5317,2305,89,788,1603,3456,5221,1910,3343,4597],28))
