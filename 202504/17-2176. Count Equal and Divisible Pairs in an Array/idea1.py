from typing import *

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        N = len(nums)
        count = 0
        for i in range(1, N):
            num = nums[i]
            for j in range(i):
                if i*j % k ==0 and num == nums[j]:
                    count+= 1
        return count

s = Solution()
print(s.countPairs(nums = [3,1,2,2,2,1,3], k = 2))