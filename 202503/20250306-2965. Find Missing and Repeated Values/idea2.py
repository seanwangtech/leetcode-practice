from typing import *
# time complexity O(n**2)
# space complexity O(1)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        sum1 = int(0)
        sum2 = int(0)
        n = len(grid)
        n2 = n**2
        for row in grid:
            for num in row:
                sum1+=num
                sum2+=num**2
        
        psum1 = (1+n2)*n2/2
        psum2 = n2*(n2+1)*(2*n2+1)/6
        diff1 = sum1-psum1 #a-b
        diff2 = sum2-psum2 #a**2 - B**2 = (a+b)(a-b)
        # a+b = diff2/diff1
        # a-b = diff1
        return [int((diff2/diff1+diff1)/2), int((diff2/diff1-diff1)/2)]

print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))