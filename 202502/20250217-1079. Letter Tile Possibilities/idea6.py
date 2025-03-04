from tokenize import group
from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        groupedTiles = {}
        for t in tiles:
            groupedTiles[t] = groupedTiles[t]+1 if groupedTiles.get(t) is not None else 1
        def countPossibilites(groupedTiles:dict)->int:
            count = 0   
            for k,tn in groupedTiles.items():
                if(tn>0):
                    groupedTiles[k] -= 1
                    count += 1 + countPossibilites(groupedTiles)
                    groupedTiles[k] += 1
            return count
        return countPossibilites(groupedTiles)

s = Solution()
print(s.numTilePossibilities('AAAAABBBCC'))