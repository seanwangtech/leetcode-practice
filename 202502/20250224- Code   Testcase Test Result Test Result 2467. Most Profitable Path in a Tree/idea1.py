from platform import node
from typing import *

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        bobPath = self.getBobPath(edges, bob)   #O(n^2)
        possibleIncomes = []
        def helper(curNode = 0, preNode = -1, step = 0, income = 0): # time O(n^2)
            nonlocal bobPath, possibleIncomes
            adjacents = self.getAdjacent(edges, curNode)
            curIncome = amount[curNode]
            if(step<len(bobPath)) and (bobPath[step] == curNode):
                curIncome = curIncome // 2
            elif(curNode in bobPath[:step]):    #O(n)
                curIncome = 0
            income += curIncome
            if(curNode !=0 and len(adjacents)<=1):
                # leaf nodes
                possibleIncomes.append(income)
                return
            for node in adjacents:
                if(node != preNode):
                    helper(node, curNode, step+1, income)
        helper()
        return max(possibleIncomes)


    def getAdjacent(self, edges:List[List[int]], nodeId):
        # time: O(n), can be optimized
        ret = []
        for i,j in edges:
            if i == nodeId:
                ret.append(j)
            if j == nodeId:
                ret.append(i)
        return ret

    def getBobPath(self, edges:List[List[int]], bob:int):
        # time complexity O(n^2), int the worest case, all of nodes was access, and perform getAdjancet once per node. 
        ret = []
        def helper(curNode, preNode = -1) -> bool:
            ret.append(curNode)
            if(curNode == 0):
                return True
            adjacents = self.getAdjacent(edges, curNode)
            for node in adjacents:
                if(node != preNode):
                    if helper(node, curNode):
                        return True
            ret.pop()
            return False
        helper(bob)
        return ret



s = Solution()
# print(s.getAdjacent([[0,1],[1,2],[1,3],[3,4]], 4))
# print(s.getBobPath([[0,1],[1,2],[1,3],[3,4]], 3 ))
# print(s.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))
print(s.mostProfitablePath([[0,2],[1,4],[1,6],[2,4],[3,6],[3,7],[5,7]], 4, [-6896,-1216,-1208,-1108,1606,-7704,-9212,-8258]))