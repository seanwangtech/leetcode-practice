from typing import *
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ops = [0]*N
        count = 0
        for i in range(N-2):
            if nums[i] ^ ops[i] == 0:
                ops[i+1] ^= 1
                ops[i+2] = 1
                count += 1
                
        if nums[-1] ^ ops[-1] == 0 or nums[-2] ^ ops[-2] == 0:
            return -1
        return count
    
s = Solution()
print(s.minOperations(nums = [0,1,1,1,0,0]))