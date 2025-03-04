from typing import *

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lower = []
        middle = []
        higher = []
        for num in nums:
            if num < pivot:
                lower.append(num)
            elif num == pivot:
                middle.append(num)
            else:
                higher.append(num)
        return lower+middle+higher
                
s = Solution()
print(s.pivotArray([9,12,5,10,14,3,10],10))