from typing import *
from collections import defaultdict

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        dictLeft = defaultdict(int)
        dictRight = defaultdict(int)
        for num in nums:
            dictRight[num] += 1
        
        for i, num in enumerate( nums):
            dictLeft[num] += 1
            dictRight[num] -= 1
            if dictLeft[num]*2 > i+1 and dictRight[num]*2 > len(nums) - (i+1):
                return i
        return -1

s = Solution()
print(s.minimumIndex([1,2,2,2]))