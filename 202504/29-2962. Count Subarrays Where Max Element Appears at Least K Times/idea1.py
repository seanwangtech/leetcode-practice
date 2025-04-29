from typing import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        maxn = max(nums)
        maxCount = 0
        left = -1
        count = 0
        for i,num in enumerate(nums):
            if num == maxn:
                maxCount+=1
                while maxCount >= k:
                    left+=1
                    while(nums[left] != maxn):
                        left += 1
                    maxCount -= 1
            count += left + 1
        return count
            
    
    
s = Solution()
print(s.countSubarrays(nums = [1,3,2,3,3], k = 2))