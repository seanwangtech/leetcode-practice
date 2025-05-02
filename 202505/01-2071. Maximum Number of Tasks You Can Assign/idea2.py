from bisect import bisect_left
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

    def isPossible(self, tasks, workers:List, pills, strength):
        for i in range(len(tasks)-1, -1, -1):
            t = tasks[i]
            if workers[-1] >= t:
                workers.pop()
            else:
                if pills ==0:
                    return False
                wi = bisect_left(workers,t - strength)
                if wi == len(workers):
                    return False
                else:
                    pills -= 1
                    workers.pop(wi)
        return True

s= Solution()
print(s.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))