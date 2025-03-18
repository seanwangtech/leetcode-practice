from typing import *

# time complexity O(n), in each iteration
# space complexity O(1)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        mask = 0
        longestSubarryLen = 1
        for i in range(0,N):
            while nums[i] & mask != 0:
                mask = nums[left] ^ mask
                left += 1
            mask = mask | nums[i]
            lenSub = i - left +1
            if longestSubarryLen < lenSub:
                longestSubarryLen = lenSub
        return longestSubarryLen
    
s = Solution()
print(s.longestNiceSubarray([1,3,8,48,10]))