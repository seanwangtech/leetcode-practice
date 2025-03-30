from curses.ascii import SO


from typing import *

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i,chr in enumerate(s):
            last[chr] = i
        
        preSplit = -1
        ret = []
        curSplit = 0
        for i, chr in enumerate(s):
            curSplit = max(last[chr], curSplit)
            if i == curSplit:
                ret.append(curSplit-preSplit)
                preSplit = curSplit
        return ret


s = Solution()
print(s.partitionLabels(s = "ababcbacadefegdehijhklij"))