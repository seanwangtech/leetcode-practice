from tkinter import N
from typing import *

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        count = 1e5
        for i in range(1, 7):
            count = min(count, self.getNumPlips(tops, bottoms, i), self.getNumPlips(bottoms,tops, i))
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