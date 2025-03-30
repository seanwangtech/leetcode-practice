from curses.ascii import SO


from typing import *
from collections import defaultdict

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        for chr in s:
            freq[chr] += 1
        count = 0
        freqSub = defaultdict(int)
        ret = []
        for chr in s:
            freqSub[chr] += 1
            count += 1
            if freqSub[chr] == freq[chr]:
                freqSub.pop(chr)
            if len(freqSub) == 0:
                ret.append(count)
                count = 0
        return ret



s = Solution()
print(s.partitionLabels(s = "ababcbacadefegdehijhklij"))