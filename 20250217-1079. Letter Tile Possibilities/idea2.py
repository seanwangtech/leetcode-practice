from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 0
        used = [0]*len(tiles)
        def ntp():
            nonlocal count, used, tiles
            #pick a tile
            #use set to store has processed otpions
            po = set()
            for i,u in enumerate(used):
                if (not u) and (tiles[i] not in po):
                    po.add(tiles[i])
                    count += 1
                    used[i] = True
                    ntp()
                    used[i] = False
        ntp()
        return(count)

s = Solution()
print(s.numTilePossibilities('AAB'))