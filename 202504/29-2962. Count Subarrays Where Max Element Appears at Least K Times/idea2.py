from typing import *

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        maxn = max(nums)
        maxCount = 0
        left = 0
        count = 0
        for i,num in enumerate(nums):
            if num == maxn:
                maxCount+=1
                while maxCount >= k:
                    if(nums[left] == maxn):
                        maxCount -= 1
                    left+=1
            count += left
        return count
            
    
    
s = Solution()
print(s.countSubarrays(nums = [1,3,2,3,3], k = 2))