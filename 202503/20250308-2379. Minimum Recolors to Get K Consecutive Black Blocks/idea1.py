from collections import deque

# time complexity: O(n)
# space complexity: O(k)
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        nw = 0
        q = deque()
        minOP = k
        for chr in blocks:
            q.append(chr)
            if(chr=='W'):
                nw += 1
            if(len(q)==k):
                if(nw<minOP):
                    minOP = nw
                chrl = q.popleft()
                if(chrl =='W'):
                    nw -= 1
        return minOP
                

s = Solution()
print(s.minimumRecolors('WBBWWBBWBW', 7))