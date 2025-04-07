from typing import *

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        total = sum(nums)
        if total%2 != 0:
            return False
        else:
            half = total//2
        seen = [False]*(half+1)  # space < O(half)
        seen[0] = True
        for num in nums:
            if num <= half:
                if(seen[half-num]):
                    return True
                else:
                    for i in range(half-num, -1, -1):
                        if seen[i]:
                            seen[i+num]= True
        return False
        
    
    
s = Solution()
# print(s.canPartition([1,5,11,5]))
# print(s.canPartition([3,3,3,4,5]))
# print(s.canPartition([1,2,3,4,5,6,7]))
print(s.canPartition([1,2,5]))