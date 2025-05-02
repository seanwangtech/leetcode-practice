from typing import *
import heapq

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks.sort()
        workers.sort()
        left = 0
        right = min(len(tasks), len(workers))
        while left<=right:
            mid = (left+right)//2
            if(self.isPossible(tasks[:mid], workers[-mid:], pills, strength)):
                left = mid +1
            else:
                right = mid -1
        return right

    def isPossible(self, tasks, workers, pills, strength):
        workersMeta = [(w, False) for w in workers]
        heapq.heapify(workersMeta)
        for i in range(len(tasks)):
            t = tasks[i]
            w, pillTaken = heapq.heappop(workersMeta)
            while t>w:
                if (pillTaken or pills==0):
                    return False
                pills -= 1
                heapq.heappush(workersMeta,(w+strength, True))
                w, pillTaken = heapq.heappop(workersMeta)
        return True

s= Solution()
print(s.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))