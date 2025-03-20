from typing import List

class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        N = len(points)
        xDict = {}
        yDict = {}
        xySet = set()
        minArea = 0
        for i in range(N):
            x,y = points[i]
            if i>2:
                for y1 in xDict.get(x,[]):
                    for x1 in yDict.get(y,[]):
                        if x1!=x and y1!=y and ((x1,y1) in xySet):
                            area = abs((x-x1)*(y-y1))
                            minArea = area if minArea == 0 else min(minArea, area)
            xDict[x] = xDict.get(x,[])+[y]
            yDict[y] = yDict.get(y,[]) + [x]
            xySet.add((x,y))
        return minArea
    
s = Solution()
print(s.minAreaRect([[1,1],[1,3],[3,1],[3,3],[2,2]]))
print(s.minAreaRect([[0,1],[1,3],[3,3],[4,4],[1,4],[2,3],[1,0],[3,4]]))