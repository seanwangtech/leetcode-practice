from typing import *

# time complexity O(nlogn)
# space complexity O(1)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        start, split, end = 0,len(nums),len(nums)
        result = ""
        for ith in range(len(nums)):
            i = start
            while(True):
                if(i==split):
                    break
                if(nums[i][ith] == '0'):
                    i += 1
                else:
                    split -=1
                    nums[i], nums[split] = nums[split], nums[i]
            if split-start <= end - split:
                end = split
                result = result + '0'
            else:
                start, split = split, end
                result = result + '1'
        return result
        
s = Solution()
print(s.findDifferentBinaryString(["01","10"]))
print(s.findDifferentBinaryString(["111","011","001"]))