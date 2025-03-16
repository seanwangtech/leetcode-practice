from typing import *
# time complexity = O(N*M)
# space complexity = O(N)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        assigns = [0]*N
        timeTake = 0
        for _ in range(cars):
            timeTake = float('inf')
            minIndex = 0
            for i in range(N):
                if timeTake > (assigns[i]+1)**2 * ranks[i]:
                    minIndex = i
                    timeTake = (assigns[i]+1)**2 * ranks[i]
            assigns[minIndex] +=1
        return timeTake

s = Solution()
print(s.repairCars([4,2,3,1], 10))