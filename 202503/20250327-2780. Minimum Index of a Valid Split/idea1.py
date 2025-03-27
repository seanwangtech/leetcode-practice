from typing import *

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)
        x = self.findDominantElectment(nums)
        count = 0
        splitCandidate = 0
        for i in range(N):
            if nums[i] == x:
                count+=1
            if count > (i+1)//2:
                splitCandidate = i
                break
        count = 0
        for i in range(i+1, N):
            if nums[i] == x:
                count+=1
        
        if count> (N - (splitCandidate+1))//2:
            return splitCandidate
        else:
            return -1


    def findDominantElectment(self, nums: List[int]) -> int:
        majorElement =0
        count =0
        for num in nums:
            if count == 0:
                majorElement = num

            if majorElement == num:
                count += 1
            else:
                count -=1
        return majorElement

s = Solution()
print(s.minimumIndex([1,2,2,2]))