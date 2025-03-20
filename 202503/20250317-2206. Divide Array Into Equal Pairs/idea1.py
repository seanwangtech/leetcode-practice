from typing import List

from collections import Counter

# time complexity O(n)
# space complexity O(n)
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nonPaired = set()
        for n in nums:
            if n in nonPaired:
                nonPaired.remove(n)
            else:
                nonPaired.add(n)
        return len(nonPaired) == 0

s = Solution()
print(s.divideArray([3,2,3,2,2,2]))