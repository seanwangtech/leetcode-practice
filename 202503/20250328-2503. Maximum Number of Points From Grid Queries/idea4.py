from typing import *
import heapq 

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        M, N = len(grid), len(grid[0])
        directions = [(-1,0), (1, 0), (0, -1), (0, 1) ]
        qsort = [(q,i) for i,q in enumerate(queries)]
        qsort.sort()
        ret = [0]*len(qsort)
        queue = [(grid[0][0], 0, 0)]
        visited = set()
        count = 0
        for q, i in qsort:
            while queue and queue[0][0]<q:
                num,y,x = heapq.heappop(queue)

                if (y,x) in visited:
                    continue
                visited.add((y,x))
                count += 1
                for dy, dx in directions:
                    y1,x1 = y+dy, x+dx
                    if x1>=0 and x1<N and y1>=0 and y1 < M:
                        heapq.heappush(queue,(grid[y1][x1], y1, x1))
            ret[i] = count
        return ret
        
s = Solution()
print(s.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))