from typing import *
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        na = 0
        precolor = colors[0]
        count = 0
        N = len(colors)
        for i in range(1,N+k-1):
            c = colors[i%N]
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