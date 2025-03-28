from typing import *
import heapq 

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        directions = [(-1,0), (1, 0), (0, -1), (0, 1) ]
        qsort = queries.copy()
        qsort.sort()
        ret_temp = [0]*len(qsort)
        queue = [(grid[0][0], 0, 0)]
        seen = set()
        count = 0
        for i, q in enumerate(qsort):
            while queue and queue[0][0]<q:
                num,y,x = heapq.heappop(queue)

                if (y,x) in seen:
                    continue
                seen.add((y,x))
                count += 1
                for dy, dx in directions:
                    y1,x1 = y+dy, x+dx
                    if(y1<0 or y1>= len(grid)):
                        continue
                    if(x1<0 or x1>= len(grid[0])):
                        continue
                    heapq.heappush(queue,(grid[y1][x1], y1, x1))
            ret_temp[i] = count
        resultDict = dict(zip(qsort, ret_temp))
        return [resultDict[q] for q in queries]
        
s = Solution()
print(s.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))