from typing import *

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        xm = {}
        ym = {}
        for xs, ys, xe, ye in rectangles:
            xm[xs] = max(xm.get(xs, xs), xe)
            ym[ys] = max(ym.get(ys, ys), ye)
        return self.check(xm) or self.check(ym)
    def check(self, xm:dict):
        split_count = -1
        pre_end = -1
        for start,end in sorted(xm.items()):
            if start >= pre_end:
                split_count += 1
            if end> pre_end:
                pre_end = end
            if split_count >=2:
                return True
        return False
        
        
s = Solution()
# print(s.checkValidCuts(5, [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]))
print(s.checkValidCuts(4, [[0,0,1,4],[1,0,2,3],[2,0,3,3],[3,0,4,3],[1,3,4,4]]))