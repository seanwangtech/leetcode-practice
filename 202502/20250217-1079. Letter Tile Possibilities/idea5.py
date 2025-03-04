from typing import *
import collections
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        groupedTiles = collections.Counter(tiles)
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