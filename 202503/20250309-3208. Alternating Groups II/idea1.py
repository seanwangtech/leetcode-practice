from typing import *
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        na = 0
        precolor = colors[-k+1]
        count = 0
        for c in colors[-k+1:]:
            if(precolor != c):
                na+=1
            else:
                na = 0
            precolor = c
        for c in colors:
            if(precolor != c):
                na+=1
            else:
                na = 0
            precolor = c
            if(na >= k-1):
                count+=1
        return count

s = Solution()
print(s.numberOfAlternatingGroups([0,1,0,1,0], 3))