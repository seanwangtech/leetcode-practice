from typing import *

# time complexity: O(N*M)
# space complexity: O(1)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        maxSteps = -1
        for i in range(N): #O(N)
            num = nums[i]
            steps = 0
            while num>0: #O(M)
                if(steps == M):
                    return -1
                q = queries[steps]
                if (i>= q[0] and i<= q[1]):
                    num -= q[2]
                steps += 1
            maxSteps = max(maxSteps,steps)
        return maxSteps
    
s=Solution()
print(s.minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]]))