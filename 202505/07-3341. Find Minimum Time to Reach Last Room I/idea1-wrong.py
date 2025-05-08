from typing import *
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        N = len(moveTime)
        M = len(moveTime[0])
        dp = [[float('inf')]*M for i in range(N)]
        for ni in range(0,N):
            for mi in range(M):
                if ni==0 and mi==0:
                    dp[0][0]=0
                else:
                    dp[ni][mi] = max(min(dp[ni-1][mi], dp[ni][mi-1]), moveTime[ni][mi])+1
        print(dp)
        return dp[-1][-1] 
        
s = Solution()
print(s.minTimeToReach([[0,0,0],[0,0,0]]))