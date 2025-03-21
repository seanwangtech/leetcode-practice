from heapq import heappush
from typing import *
# n is number edges
# time complexity: O(n*n)
# space complexity: O(n)
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        edgesMap = {}
        for u,v,w in edges:
            edgesMap[u] = edgesMap.get(u,[]) + [(v,w)]
            edgesMap[v] = edgesMap.get(v,[]) + [(u,w)]
        ret = []
        for s,t in query:
            cost = self.costOf(s,t, edgesMap)
            ret.append(cost)
        return ret
    def costOf(self, s,t, edgesMap:dict):
        cost = ~0
        visted = set()
        def helper(node):
            nonlocal visted, cost
            if node in visted:
                return
            visted.add(node)
            for c,w in edgesMap.get(node,[]):
                helper(c)
                cost &= w
        helper(s)
        if t in visted:
            return cost
        else:
            return -1

s = Solution()
print(s.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(s.minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))