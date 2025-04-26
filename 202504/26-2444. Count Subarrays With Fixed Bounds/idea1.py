from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        N = len(nums)
        ioutBound = -1
        imin = -1
        imax = -1
        count = 0
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                ioutBound = i
            if num == minK: 
                imin = i
            if num == maxK:
                imax = i
            subcount = min(imin, imax)-ioutBound
            if subcount>0:
                count += subcount
        return count

s = Solution()
print(s.countSubarrays(nums = [1,3,5,2,7,5], minK = 1, maxK = 5))
print(s.countSubarrays(nums = [1,1,1,1], minK = 1, maxK = 1))