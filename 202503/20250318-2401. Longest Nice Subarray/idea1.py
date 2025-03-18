from typing import *

# time complexity O(n), in each iteration, it should be up to log(2, 10^9) -- 29 bits. O(29*n) -> O(n)
# space complexity O(1)

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        longestSubarry = 1
        ipre = 0
        for i in range(1,N):
            j = i-1
            while(j>=ipre):
                if nums[i]&nums[j] != 0:
                    ipre = j+1
                j -= 1
            lenSub = i - ipre +1
            if longestSubarry < lenSub:
                longestSubarry = lenSub
        return longestSubarry
    
s = Solution()
print(s.longestNiceSubarray([1,3,8,48,10]))