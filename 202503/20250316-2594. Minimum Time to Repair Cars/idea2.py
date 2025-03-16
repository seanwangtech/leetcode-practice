from typing import *
import heapq
# time complexity = O(N*M)
# space complexity = O(N)
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        N = len(ranks)
        timePredicts = [(x, 0) for x in ranks]
        heapq.heapify(timePredicts)
        timeTake = 0
        for _ in range(cars):
            nextTime, waitCar = heapq.heappop(timePredicts)
            waitCar = waitCar+1
            timeTake =nextTime
            heapq.heappush(timePredicts, ((nextTime//waitCar**2)*(waitCar+1)**2, waitCar))
        return timeTake

s = Solution()
print(s.repairCars([4,2,3,1], 10))