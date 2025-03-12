#time complexity O(log(n))
#space complexity O(1)
from typing import *
class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # binary search
        left, right = (-1,len(nums))
        while(right-left>1):
            mid = (right+left)//2
            if nums[mid]<0:
                left = mid
            else:
                right = mid
        n_neg = right
        
        left, right = (-1,len(nums))
        while(right-left>1):
            mid = (right+left)//2
            if nums[mid]>0:
                right = mid
            else:
                left = mid
        n_pos = len(nums) - right
        return max(n_neg, n_pos)
        
    
s = Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))