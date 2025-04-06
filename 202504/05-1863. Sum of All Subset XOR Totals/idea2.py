from typing import *

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        N = len(nums)
        def helper(index=0, xors =  0):
            nonlocal N
            if index == N:
                return xors
            return helper(index+1, xors) + helper(index+1, xors ^ nums[index])
        return helper()
s = Solution()
print(s.subsetXORSum(nums = [1,3]))
print(s.subsetXORSum(nums = [5,1,6]))