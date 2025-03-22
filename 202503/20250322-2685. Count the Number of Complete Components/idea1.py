from typing import *

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        N = n
        parents = [-1]*N
        componts = {x:(1,0) for x in range(N)} 
        
        def find(node) -> int:
            nonlocal parents
            if(parents[node] == -1):
                return node
            
            parents[node] =  find(parents[node])
            return parents[node]
        
        def union(a,b):
            nonlocal parents, componts
            a_parent = find(a)
            b_parent = find(b)
            
            if a_parent == b_parent:
                an, aEdge = componts.get(a_parent,(1, 0))
                componts[a_parent] = (an, aEdge+1)
            
            else:
                an, aEdge = componts.get(a_parent,(1, 0))
                bn, bEdge = componts.get(b_parent,(1, 0))
                if an>=bn:
                    componts[a_parent] = (an+bn, aEdge+bEdge+1)
                    parents[b_parent] = a_parent
                    componts.pop(b_parent,-1)
                else:
                    componts[b_parent] = (an+bn, aEdge+bEdge+1)
                    parents[a_parent] = b_parent
                    componts.pop(a_parent,-1)
        for a,b in edges:
            union(a,b)
        # print(componts)
        # print(parents)
        complete_connected_components = 0
        for n, edge in componts.values():
            if(edge == n*(n-1)/2):
                complete_connected_components+= 1
        return complete_connected_components
   
    

    
s = Solution()
print(s.countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]] ))
