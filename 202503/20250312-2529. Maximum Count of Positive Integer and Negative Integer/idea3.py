from typing import *

#time complexity O(log(n))
#space complexity O(1)

class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        print(self.lowerbound(nums))
        print(self.upperbound(nums))
        return max(self.lowerbound(nums), len(nums)-self.upperbound(nums))
    def lowerbound(self, nums):
        # binary search
        li,hi = 0, len(nums)-1
        index = len(nums)
        while li<=hi:
            mid = (li+hi)//2
            if nums[mid] < 0:
                li = mid +1
            else:
                hi = mid -1
                index = mid
        return index
    def upperbound(self, nums):
        # binary search
        li,hi = 0, len(nums)-1
        index = len(nums)
        while li<=hi:
            mid = (li+hi)//2
            if nums[mid] <= 0:
                li = mid +1
            else:
                hi = mid -1
                index = mid
        return index
    
s = Solution()
print(s.maximumCount([-2,-1,-1,1,2,3]))
print(s.maximumCount([-2,-1,-1]))
print(s.maximumCount([0,0,0]))