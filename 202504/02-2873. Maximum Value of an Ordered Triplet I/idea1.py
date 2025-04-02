from typing import *

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        N = len(nums)
        premax = max(nums[:2])
        prediffmax = nums[0]-nums[1]
        val = -float('inf')
        for i in range(2, N):
            num = nums[i]
            newVal = prediffmax * num
            val = max(val, newVal)
            premax = max(premax, num)
            prediffmax = max(prediffmax, premax-num)
        return val if val>0 else 0

s = Solution()
print(s.maximumTripletValue(nums = [12,6,1,2,7]))