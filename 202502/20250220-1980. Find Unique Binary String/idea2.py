from typing import *

# time complexity O(n)
# space complexity O(1)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        start, split, end = 0,len(nums),len(nums)
        result = ""
        for i in range(len(nums)):
            result = result + ('1' if nums[i][i] == '0' else '0' )
        return result
        
s = Solution()
print(s.findDifferentBinaryString(["01","10"]))
print(s.findDifferentBinaryString(["111","011","001"]))