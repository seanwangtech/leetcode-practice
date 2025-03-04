from typing import *

# time complexity O(n^2)
# space complexity O(n)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        def helper(nums, ans):
            nonlocal n
            if (len(ans) == n): 
                if(ans not in nums): #(O(n))
                    return ans
                return None
            return helper(nums, ans + '0' ) or helper(nums, ans + '1')
        return helper(nums, '')
        
s = Solution()
print(s.findDifferentBinaryString(["00","01"]))
print(s.findDifferentBinaryString(["111","011","001"]))

