from typing import *

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k ==1:
            return 0
        N = len(weights)
        pairSum = [weights[i]+weights[i+1] for i in range(N-1)]
        pairSum.sort()
        return sum(pairSum[-(k-1):]) - sum(pairSum[:k-1])

s = Solution()
print(s.putMarbles(weights = [1,3,5,1], k = 2))