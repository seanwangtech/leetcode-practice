from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        if len(tiles) == 0:
            return 0
        tilesGrouped = {}
        for t in tiles:
            tilesGrouped[t] = tilesGrouped.get(t, 0) +1
        # get numbers of each tiles type, remove letters information and keep a list of number. 
        # e.g. for the sequence "AABBBC", it will converted to dict {'A':2, 'B':3, 'C':1}, then to list [2,3,1]
        tilesAbs = list(tilesGrouped.values())
        tilesAbsChosen = [0]*len(tilesAbs)
        count = 0         
        done = False
        while (not done):
            chosen = self.remove0Value(tilesAbsChosen)
            if(len(chosen)>0):
                count += self.countPermutations(chosen)
            # add one 
            ith=len(tilesAbs) -1
            while(True):
                if(ith <0):
                    done = True
                    break
                if(tilesAbsChosen[ith]<tilesAbs[ith]):
                    tilesAbsChosen[ith] += 1
                    break
                else:
                    tilesAbsChosen[ith] = 0
                    ith -= 1
        return(count)
    
    def remove0Value(self, arr):
        chosen = []
        for ts in arr:
            if(ts>0):
                chosen.append(ts)
        return chosen
    def factorial(self, n:int)->int:
        if(n<1):
            return
        for i in range(n-1, 0, -1):
            n *= i
        return n
    def countPermutations(self, arr:int)->int:
        # O(n)
        dividend = self.factorial(sum(arr))
        divisior = 1
        for i in range(len(arr)):
            divisior *= self.factorial(arr[i])
        return dividend//divisior
    

s = Solution()
print(s.numTilePossibilities('AABB'))