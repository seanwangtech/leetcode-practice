from typing import *
import heapq 

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        qsort = queries.copy()
        qsort.sort()
        ret_temp = [0]*len(qsort)
        queue = [(0, 0, 0)]
        seen = set()
        count = 0
        while queue:
            qi,y,x = heapq.heappop(queue)
            q = qsort[qi]
            if(y<0 or y>= len(grid)):
                continue
            if(x<0 or x>= len(grid[0])):
                continue
            if (y,x) in seen:
                continue
            if grid[y][x] >= q:
                if qi+1 <  len(qsort):
                    heapq.heappush(queue,(qi+1, y, x)) # this may not efficient, each round of check can involve massive number of qi+1
                continue
            seen.add((y,x))
            count += 1
            heapq.heappush(queue,(qi, y-1, x))
            heapq.heappush(queue,(qi, y+1, x))
            heapq.heappush(queue,(qi, y, x-1))
            heapq.heappush(queue,(qi, y, x+1))
            ret_temp[qi] = count
        resultDict = dict(zip(qsort, ret_temp))
        return [resultDict[q] for q in queries]
        
s = Solution()
print(s.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))