from bisect import bisect_left
from typing import *
import heapq
from collections import deque

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
        potentialWorkers = deque()
        for i in range(len(tasks)-1, -1, -1):
            t = tasks[i]
            while len(workers) >0 and workers[-1]+strength>=t:
                potentialWorkers.append(workers.pop())
            if len(potentialWorkers)==0:
                return False
            if potentialWorkers[0]>=t:
                # can do the task without a pill
                potentialWorkers.popleft()
            else:
                # need pill to do the work, pick minimium strength worker can do with a pill
                if pills==0:
                    return False
                pills-=1
                potentialWorkers.pop()

        return True

s= Solution()
print(s.maxTaskAssign(tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1))