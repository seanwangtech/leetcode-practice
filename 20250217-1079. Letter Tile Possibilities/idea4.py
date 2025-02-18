from tokenize import group
from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        groupedTiles = {}
        for t in tiles:
            groupedTiles[t] = groupedTiles[t]+1 if groupedTiles.get(t) is not None else 1
        count = 0
        def countPossibilites():
            nonlocal groupedTiles, count
            for k,tn in groupedTiles.items():
                if(tn>0):
                    groupedTiles[k] -= 1
                    count += 1
                    countPossibilites()
                    groupedTiles[k] += 1
        countPossibilites()
        return count

s = Solution()
print(s.numTilePossibilities('ACCCCCD'))