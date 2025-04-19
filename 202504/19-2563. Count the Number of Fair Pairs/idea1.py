from typing import *

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        N = len(nums)
        left=right=N-1
        count = 0
        for i, num in enumerate(nums):
            while left >= 0 and nums[left]+num>=lower:
                left -= 1
            while right >=0 and nums[right]+num > upper:
                right -= 1
            count += right - left
            if i > left and i<= right:
                count -= 1
        return count//2

s = Solution()
print(s.countFairPairs(nums = [0,1,7,4,4,5], lower = 3, upper = 6))