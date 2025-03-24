from typing import *

class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        diffList = [0] * (days + 2)
        for start, end in meetings:
            diffList[start] +=1
            diffList[end+1] -=1
            
        presum = 0
        count = 0
        for i in range(1,days+1):
            presum += diffList[i]
            if presum == 0:
                count += 1
                
        return count
        

s = Solution()
print(s.countDays(days = 10, meetings = [[5,7],[1,3],[9,10]]))