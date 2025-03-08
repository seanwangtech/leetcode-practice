from typing import *
# time complexity O(n**2)
# space complexity O(n**2)
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        checkSet = set(range(1,n**2+1))
        for row in grid:
            for num in row:
                if(num not in checkSet):
                    a = num
                else:
                    checkSet.remove(num)
        b = checkSet.pop()
        return [a,b]

print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))