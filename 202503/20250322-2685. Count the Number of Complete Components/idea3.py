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
            a_root = find(a)
            b_root = find(b)
            
            if a_root == b_root:
                # Find root of component with path compression
                an, aEdge = componts.get(a_root,(1, 0))
                componts[a_root] = (an, aEdge+1)
            
            else:
                an, aEdge = componts.get(a_root,(1, 0))
                bn, bEdge = componts.get(b_root,(1, 0))
                # Merge smaller component into larger one
                if an < bn:
                    a_root,b_root = b_root,a_root
                componts[a_root] = (an+bn, aEdge+bEdge+1)
                parents[b_root] = a_root
                componts.pop(b_root,-1)
        for a,b in edges:
            union(a,b)
        complete_connected_components = 0
        for n, edge in componts.values():
            if(edge == n*(n-1)//2):
                complete_connected_components+= 1
        return complete_connected_components
    
s = Solution()
print(s.countCompleteComponents(6,[[0,1],[0,2],[1,2],[3,4]] ))
