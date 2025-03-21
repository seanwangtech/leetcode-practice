from cmath import cos
from collections import deque
from heapq import heappush
from typing import *

# time complexity: O(max(n,m)+q)
# space complexity: O(max(n.m)+q)
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        clusters = {}
        edgesMap = {}
        for u,v,w in edges:
            edgesMap[u] = edgesMap.get(u,[]) + [(v,w)]
            edgesMap[v] = edgesMap.get(v,[]) + [(u,w)]
        ret = []
        for s,t in query:
            if s in clusters:
                sgc = clusters[s]
                tgc = clusters.get(t, (-1,-1))
                if(sgc[0] == tgc[0]):
                    ret.append(sgc[1])
                else:
                    ret.append(-1)
            else:
                cost, visited = self.costOf(s, edgesMap)
                group_cost = (s, cost)
                for vt in visited:
                    clusters[vt] = group_cost
                if(t in visited):
                    ret.append(cost)
                else:
                    ret.append(-1)
        return ret

    def costOf(self, s, edgesMap:dict):
        cost = ~0
        visted = set()
        stack = [s]
        while stack:
            node = stack.pop()
            if(node in visted):
                continue
            visted.add(node)
            for c,w in edgesMap.get(node,[]):
                stack.append(c)
                cost &= w
        return cost, visted

s = Solution()
print(s.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(s.minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))