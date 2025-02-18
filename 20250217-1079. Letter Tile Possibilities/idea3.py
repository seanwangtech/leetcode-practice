from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        groupedTiles = {}
        for t in tiles:
            groupedTiles[t] = groupedTiles[t]+1 if groupedTiles.get(t) is not None else 1
        tilesAbs = list(groupedTiles.values())
        count = 0
        def countPossibilites():
            nonlocal tilesAbs, count
            for i, tn in enumerate(tilesAbs):
                if(tn>0):
                    tilesAbs[i] -= 1
                    count += 1
                    countPossibilites()
                    tilesAbs[i] += 1
        countPossibilites()
        return count

s = Solution()
print(s.numTilePossibilities('AAB'))