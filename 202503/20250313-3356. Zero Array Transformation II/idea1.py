from typing import *

# time complexity: O(N*M)
# space complexity: O(1)
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        M = len(queries)
        if(max(nums) <=0): #O(N)
            return 0
        for i in range(M): #O(M)
            q = queries[i]
            for j in range(q[0], q[1]+1):#O(N)
                nums[j]-= q[2]
            if(max(nums) <=0): #O(N) -- this not efficient
                return i+1
        return -1
    
s=Solution()
print(s.minZeroArray([2,0,2],[[0,2,1],[0,2,1],[1,1,3]]))