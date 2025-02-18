from tokenize import group
from typing import *

# try to rewrite idea 4 by iterative method without recursion
# the iterative way need to manage backtracking manually, which need to manually save and retrive the backtracking info (local varaible in recursion) alone with pop push. 
# So it's not intuitive to understand. 
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        groupedTiles = {}
        for t in tiles:
            groupedTiles[t] = groupedTiles[t]+1 if groupedTiles.get(t) is not None else 1
        count = 0
        def countPossibilites():
            nonlocal groupedTiles, count
            stack = []
            stack.append({'it':iter(groupedTiles.keys())}) # in idea 4, the iterator is save in call stack automatically, here we need to manually manage it.
            while len(stack) >0:
                args = stack.pop()
                if(args.get('k') is not None):
                    # this is minic after function-call-break code. 
                    # in idea 4, there is one function call break the code, what if there is multiple function break? In this case, it would even more complicated flow control and status to 
                    # handle backtracking info and resume after break. Considering the nature difference between recursion and iterative way, although theoretically 
                    # they are interchangeable, in practice, it's complicated, because:
                    # 1. the flow control and procedure end condition of the iterative algorithm is straightforward, no complex flow break and resume. If a complex recousive function call break, it can be challenge to manage the status and backtracking info/variables.
                    # 2. the recoursion algoirthm has can hanle complex break (good hanle complex exploring with natually backtracking), how every, flow control and procedure end condition may not intuitive. 
                    # Both algorithm have their own advantage and disadvantage. Understanding these features helps to choose the right one for a specific problem.
                    # in idea 4, the local variable k is save in call stack automatically, here we need to manually manage it.
                    # to put back tiles after pop from stack if k is set. 
                    groupedTiles[args['k']] += 1
                it = args['it']  # retrive the iterator from call stack
                for k in it:
                    if(groupedTiles[k]>0):
                        groupedTiles[k] -= 1
                        args['k'] = k
                        count += 1
                        stack.append(args) # save the backtracking info 
                        stack.append({'it':iter(groupedTiles.keys())}) # put another item to stack (minic fuction call)
                        break
        countPossibilites()
        return count

s = Solution()
print(s.numTilePossibilities('AAB'))