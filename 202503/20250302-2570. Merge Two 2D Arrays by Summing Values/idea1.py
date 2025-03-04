from typing import *

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ret = []
        i1 = 0
        i2 = 0
        while(True):
            if i1== len(nums1) or i2== len(nums2):
                for id,val in nums1[i1:]:
                    ret.append[[id,val]]
                for id,val in nums2[i2:]:
                    ret.append[[id,val]]
                break

            id1,val1 = nums1[i1]
            id2,val2 = nums2[i2]

            if id1<id2:
                ret.append([id1,val1])
                i1+=1
            elif id1 == id2:
                ret.append([id1,val1+val2])
                i1+=1
                i2+=1
            else:
                ret.append([id2,val2])
                i2+=1
        return ret

s = Solution()
print(s.mergeArrays([[1,2],[2,3],[4,5]],[[1,4],[3,2],[4,1]]))