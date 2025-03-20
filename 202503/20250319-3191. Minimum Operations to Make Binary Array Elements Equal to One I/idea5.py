from typing import *
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        ops = [0]*3
        count = 0
        for i in range(N):
            ops[i%3] = 0
            if (nums[i] + sum(ops))%2 == 0:
                ops[i%3] = 1
                count += 1
                if(i>= N-2):
                    return -1
        return count
    
s = Solution()
print(s.minOperations(nums = [0,1,1,1,0,0]))