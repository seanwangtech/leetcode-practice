from typing import *

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        diffDict = {days+1:0}
        for start, end in meetings:
            diffDict[start] = diffDict.get(start, 0) + 1
            diffDict[end+1] =diffDict.get(end+1, 0) - 1
        preIndex = 1
        presum = 0
        count = 0
        for i in sorted(diffDict.keys()):
            if presum == 0:
                count += i-preIndex
            presum += diffDict[i]
            preIndex = i
                
        return count
        

s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))