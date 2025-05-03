from tkinter import N
from typing import *

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count = 1e5
        countstop = [0]*6
        countsbottom = [0]*6
        N = len(tops)
        for num in tops:
            countstop[num-1] += 1
        for num in bottoms:
            countsbottom[num-1] += 1
        
        for i in range(6):
            if countstop[i]>= N/2:
                count = min(count, self.getNumPlips(tops, bottoms, i+1))
            if countsbottom[i]>=N/2:
                count = min(count, self.getNumPlips(bottoms, tops, i+1))
        return -1 if count ==1e5 else count

    def getNumPlips(self, arr1, arr2, num):
        count = 0
        for i in range(len(arr1)):
            if arr1[i] != num:
                if arr2[i] == num:
                    count += 1
                else:
                    return 1e5
        return count

s = Solution()
print(s.minDominoRotations(tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]))
print(s.minDominoRotations(tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]))