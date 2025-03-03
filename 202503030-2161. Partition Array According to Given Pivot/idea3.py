from typing import *

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ret = [0]*len(nums)
        ilower = 0
        ihigher = len(nums)-1
        for i in range(len(nums)):
            if nums[i] < pivot:
                ret[ilower] = nums[i]
                ilower += 1
            if nums[-1-i] > pivot:
                ret[ihigher] = nums[-1-i]
                ihigher -= 1
        for i in range(ilower, ihigher+1):
            ret[i]=pivot
        return ret
s = Solution()
print(s.pivotArray([9,12,5,10,14,3,10],10))