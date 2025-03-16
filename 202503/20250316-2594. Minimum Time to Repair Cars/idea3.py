from typing import *
import heapq
from collections import Counter
import math
# time complexity = O(log(N)*M)
# space complexity = O(N)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        counts = Counter(ranks)
        left,right = 0, max(counts)*(cars//N+1)**2
        while left<=right:
            mid = (left+right)//2
            if(self.canFix(counts, cars, mid)):
                right = mid - 1
            else:
                left = mid + 1
        return left

    def canFix(self,counts, cars, time):
        total = 0
        for rank, count in counts.items():
            total += int(math.sqrt(time/rank))*count
        return cars<=total
s = Solution()
print(s.repairCars([4,2,3,1], 10))