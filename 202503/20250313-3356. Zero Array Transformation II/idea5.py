from typing import *

# time complexity: O(N+M)
# space complexity: O(N)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        diffs = [0]*(N+1)
        curMax = 0
        steps = 0
        for i in range(N): #O(N)
            num = nums[i]
            while num > diffs[i] + curMax: 
                if(steps == M):
                    return -1
                left, right, val = queries[steps]
                if(right >= i):
                    diffs[max(left, i)] += val
                    diffs[right+1] -= val
                steps += 1
            curMax += diffs[i]
        return steps
    
s=Solution()
# print(s.minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]]))
print(s.minZeroArray([0,8], [[0,1,4],[0,1,1],[0,1,4],[0,1,1],[1,1,5],[0,1,2],[1,1,4],[0,1,1],[1,1,3],[0,0,2],[1,1,3],[1,1,2],[0,1,5],[1,1,2],[1,1,5]]))