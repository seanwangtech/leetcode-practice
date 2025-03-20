from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        N = len(points)
        xySet = set()
        minArea = 0
        for i in range(N):
            x,y = points[i]
            if i>2:
                for x1, y1 in xySet:
                    if(x1 != x and y1 != y 
                       and (x,y1) in xySet and (x1,y) in xySet):
                        area = abs((x-x1)*(y-y1))
                        minArea = area if minArea == 0 else min(minArea, area)
            xySet.add((x,y))
        return minArea
    
s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]))