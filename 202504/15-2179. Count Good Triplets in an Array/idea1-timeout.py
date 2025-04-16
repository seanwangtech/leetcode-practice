from typing import *

from pyparsing import nums

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        N = len(nums1)
        pos1 = [-1]*N
        pos2 = [-1]*N
        for i in range(N):
            pos1[nums1[i]] = i
            pos2[nums2[i]] = i
        count = 0
        for y in range(N):
            p1y = pos1[y]
            p2y = pos2[y]
            countLeft = 0
            countRight = 0
            for i in range(N):
                if (pos1[i] < p1y and pos2[i]<p2y):
                    countLeft+=1
                elif (p1y < pos1[i] and p2y < pos2[i]):
                    countRight +=1 
            count += countLeft*countRight
        return count

s = Solution()
# print(s.goodTriplets(nums1 = [2,0,1,3], nums2 = [0,1,2,3]))
print(s.goodTriplets(nums1 = [13,14,10,2,12,3,9,11,15,8,4,7,0,6,5,1], nums2 = [8,7,9,5,6,14,15,10,2,11,4,13,3,12,1,0]))