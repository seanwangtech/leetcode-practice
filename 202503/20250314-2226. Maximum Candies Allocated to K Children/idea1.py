from typing import *

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        low,high = 1, sum(candies)//k
        while(low<=high):
            mid = (low+high)//2
            if self.canAllocate(candies, k, mid):
                low = mid + 1
            else:
                high = mid -1
        return low -1
    
    def canAllocate(self, candies: List[int], k: int, nCandies) -> bool:
        count = 0
        for cnds in candies:
            count += cnds //nCandies
        return count>=k
    
s = Solution()
print(s.maximumCandies(candies = [5,8,6], k = 3))