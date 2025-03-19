from typing import *
from collections import deque

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        flipQueue = deque()
        count = 0
        for i in range(N):
            while(len(flipQueue) >0 and flipQueue[0] +2 < i ):
                flipQueue.popleft()
            
            if (len(flipQueue)+nums[i])%2 ==0:
                # need to flip
                if(i+2 >= N):
                    return -1
                flipQueue.append(i)
                count += 1
        return count
    
s = Solution()
print(s.minOperations(nums = [0,1,1,1,0,0]))