from typing import *
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ops = [0]*2
        count = 0
        for i in range(N):
            if (nums[i] ^ ops[0] ^ ops[1]) == 0:
                ops[i%2] = 1
                count += 1
                if(i>= N-2):
                    return -1
            else:
                ops[i%2] = 0
        return count
    
s = Solution()
print(s.minOperations(nums = [0,1,1,1,0,0]))