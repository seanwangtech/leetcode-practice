from platform import node
from typing import *

class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        edgeDict = self.creatEdgeDict(edges)
        bobPath = self.getBobPath(edgeDict, bob)   #O(n)
        possibleIncomes = []
        def helper(curNode = 0, preNode = -1, step = 0, income = 0): # time O(n)
            nonlocal bobPath, possibleIncomes
            adjacents = edgeDict.get(curNode, [])
            curIncome = amount[curNode]
            if curNode in bobPath:
                bobStep = bobPath[curNode]
                if bobStep == step:
                    curIncome = curIncome // 2
                elif bobStep  < step:    #O(1)
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

    def creatEdgeDict(self, edges:List[List[int]]):
        ret ={}
        for i,j in edges:
            ret[i] = [*ret.get(i,[]), j]
            ret[j] = [*ret.get(j,[]), i]
        return ret

    def getBobPath(self, edgeDict:Dict, bob:int):
        # time complexity O(n), int the worest case, all of nodes was access, and perform getAdjancet once per node. 
        ret = {}
        def helper(curNode, preNode = -1, step=0) -> bool:
            ret[curNode] = step
            if(curNode == 0):
                return True
            adjacents = edgeDict.get(curNode, [])
            for node in adjacents:
                if(node != preNode):
                    if helper(node, curNode, step + 1):
                        return True
            ret.pop(curNode)
            return False
        helper(bob)
        return ret



s = Solution()
# print(s.getAdjacent([[0,1],[1,2],[1,3],[3,4]], 4))
# print(s.getBobPath([[0,1],[1,2],[1,3],[3,4]], 3 ))
# print(s.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6]))
print(s.mostProfitablePath([[0,2],[1,4],[1,6],[2,4],[3,6],[3,7],[5,7]], 4, [-6896,-1216,-1208,-1108,1606,-7704,-9212,-8258]))

