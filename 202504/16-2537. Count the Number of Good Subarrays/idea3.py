from itertools import count
from typing import *
from collections import defaultdict
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        freq = defaultdict(int)
        count = 0
        windowPairs = 0
        for num in nums:
            windowPairs+= freq[num]
            freq[num]+=1
            while windowPairs>=k:
                freq[nums[left]]-=1
                windowPairs-=freq[nums[left]]
                left+=1
            count += left
        return count

s = Solution()
print(s.countGood(nums = [3,1,4,3,2,2,4], k = 2))