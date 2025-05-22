from typing import List
import heapq

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        N = len(nums)
        candidates = []
        queries.sort()
        qOffset = 0
        diffArray = [0] * (N+1)
        presum = 0
        for i, num in enumerate(nums):
            while qOffset<len(queries) and queries[qOffset][0] <= i :
                _, right = queries[qOffset]
                heapq.heappush(candidates, -right)
                qOffset += 1
            presum += diffArray[i]
            while num > presum:
                if len(candidates) == 0:
                    return -1
                right = - heapq.heappop(candidates)
                if right >=i:
                    presum += 1
                    diffArray[right+1] -= 1
                else:
                    return -1
        return len(candidates)
    
s = Solution()
print(s.maxRemoval(nums = [2,0,2], queries = [[0,2],[0,2],[1,1]]))