from typing import *

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        
        def helper(q, y=0, x=0, seen=None):
            if seen is None:
                seen = set()
            if(y<0 or y>= len(grid)):
                return 0
            if(x<0 or x>= len(grid[0])):
                return 0
            if grid[y][x] >= q:
                return 0
            if (y,x) in seen:
                return 0
            else:
                seen.add((y,x))
                return (1+ 
                    helper(q, y-1, x, seen) + 
                    helper(q, y+1, x, seen) + 
                    helper(q, y, x-1, seen) + 
                    helper(q, y, x+1, seen)
                )
                
        return [helper(q) for q in queries]
    
s = Solution()
print(s.maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))