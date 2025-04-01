from typing import *

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0]*(N+1)
        for i in range(N-1, -1, -1):
            point, brainPower = questions[i]
            nextIndex = i+brainPower+1
            if nextIndex >= N:
                nextMaxPoint = 0
            else:
                nextMaxPoint = dp[nextIndex]
            dp[i] = max(point + nextMaxPoint, dp[i+1])
        return dp[0]

s = Solution()
print(s.mostPoints([[3,2],[4,3],[4,4],[2,5]]))