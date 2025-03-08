from collections import deque

# time complexity: O(n)
# space complexity: O(1)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        nw = 0
        minOP = k
        for i in range(len(blocks)):
            chr = blocks[i]
            if(chr=='W'):
                nw += 1
            if(i >= k-1):
                if(nw<minOP):
                    minOP = nw
                chrl = blocks[i-k+1]
                if(chrl =='W'):
                    nw -= 1
        return minOP
                

s = Solution()
print(s.minimumRecolors('WBBWWBBWBW', 7))