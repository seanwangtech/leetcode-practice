from typing import *

# time complexity: O(N+M)
# space complexity: O(M)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        maxDiff = [0]*(N+1)
        curMax = 0
        steps = 0
        for i in range(N): #O(N)
            num = nums[i]
            curMax += maxDiff[i]
            while num - curMax>0: 
                if(steps == M):
                    return -1
                q = queries[steps]
                maxDiff[q[0]] += q[2]
                maxDiff[q[1]+1] -= q[2]
                if(i>= q[0] and i<= q[1]):
                    curMax += q[2]
                steps += 1
        return steps
    
s=Solution()
# print(s.minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]]))
print(s.minZeroArray([0,8], [[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]]))