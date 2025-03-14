from typing import *
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tilesGrouped = {}
        for t in tiles:
            tilesGrouped[t] = tilesGrouped.get(t, 0) +1
        # get numbers of each tiles type, remove letters information and keep a list of number. 
        # e.g. for the sequence "AABBBC", it will converted to dict {'A':2, 'B':3, 'C':1}, then to list [2,3,1]
        tilesAbs = list(tilesGrouped.values())
        tilesAbsChosen = [0]*len(tilesAbs)
        count = 0
        def dfs(index=0):
            nonlocal tilesAbs, count
            if(index == len(tilesAbs) or tilesAbs[index] == 0):
                return
            # to calc combinations, don't need to iter from 0, start from index instead. 
            for i in range(index, len(tilesAbs)):
                tilesAbs[i] -= 1
                tilesAbsChosen[i]+=1
                chosen = self.remove0Value(tilesAbsChosen)
                if(len(chosen)>0):
                    count += self.countPermutations(chosen)
                if(tilesAbs[i] >0):
                    dfs(i)
                else:
                    dfs(i +1)
                tilesAbs[i] += 1
                tilesAbsChosen[i]-=1
        dfs()
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