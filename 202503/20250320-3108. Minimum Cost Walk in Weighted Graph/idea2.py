from heapq import heappush
from typing import *

# time complexity: O(max(n,m)+q)
# space complexity: O(max(n.m)+q)
class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        clusters = self.clustering(n, edges)
        ret = []
        for s,t in query:
            sgc = clusters[s]
            tgc = clusters[t]
            if(sgc[0] == tgc[0]):
                ret.append(sgc[1])
            else:
                ret.append(-1)
        return ret

    def clustering(self, n, edges):
        edgesMap = {}
        for u,v,w in edges:
            edgesMap[u] = edgesMap.get(u,[]) + [(v,w)]
            edgesMap[v] = edgesMap.get(v,[]) + [(u,w)]
        clusters = {}
        for node in range(n):
            if n not in clusters:
                cost, nodes = self.costOf(node, edgesMap)
                group_cost = (node, cost)
                for s in nodes:
                    clusters[s] = group_cost
        return clusters

    def costOf(self, s, edgesMap:dict):
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
        return cost, visted
            

s = Solution()
print(s.minimumCost(n = 5, edges = [[0,1,7],[1,3,7],[1,2,1]], query = [[0,3],[3,4]]))
print(s.minimumCost(3, [[0,2,7],[0,1,15],[1,2,6],[1,2,1]], [[1,2]]))