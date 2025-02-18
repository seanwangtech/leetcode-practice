from tokenize import group
from typing import *

# try to rewrite idea 4 by iterative method without recursion
# the iterative way need to manage traceback manually, which need to manually save and retrive the traceback info (local varaible in recursion) alone with pop push. 
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
                    # in idea 4, the local variable k is save in call stack automatically, here we need to manually manage it.
                    # remember to put back tiles after pop from stack if k is set. 
                    groupedTiles[args['k']] += 1
                it = args['it']
                for k in it:
                    if(groupedTiles[k]>0):
                        groupedTiles[k] -= 1
                        args['k'] = k
                        count += 1
                        stack.append(args)
                        stack.append({'it':iter(groupedTiles.keys())})
                        break
        countPossibilites()
        return count

s = Solution()
print(s.numTilePossibilities('AAB'))