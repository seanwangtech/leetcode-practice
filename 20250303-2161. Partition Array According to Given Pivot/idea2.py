from typing import *

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ret = [0]*len(nums)
        ilower = 0
        ihigher = len(nums)
        for num in nums:
            if num < pivot:
                ret[ilower] = num
                ilower += 1
            elif num > pivot:
                ihigher -= 1
        for i in range(ilower, ihigher):
            ret[i]=pivot
        for num in nums:
            if num > pivot:
                ret[ihigher]=num
                ihigher +=1
            
        return ret
s = Solution()
print(s.pivotArray([9,12,5,10,14,3,10],10))