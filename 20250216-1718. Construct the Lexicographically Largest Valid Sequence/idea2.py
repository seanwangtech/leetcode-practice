from typing import *
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        depth = 0
        maxDepth = 0
        def largestValidNum(seq:List[int], n:int):
            nonlocal depth, maxDepth
            depth += 1
            try:
                if(len(seq) == 2*n -1):
                    return seq
                for nr in range(n, 0, -1):
                    if(nr == 1):
                        if 1 not in seq:
                            return largestValidNum([*seq,1], n)
                    else:
                        nrCount = seq.count(nr)
                        if (nrCount == 0 and 2*n -1 - len(seq) > nr) or (nrCount == 1 and len(seq)>=nr and seq[-nr]==nr):
                            ret = largestValidNum([*seq, nr], n)
                            if(ret):
                                return ret
                return None

            finally:
                maxDepth = max(depth, maxDepth)
                depth-=1

        ret = largestValidNum([],n)
        print("macDepth=", maxDepth)
        return ret

s = Solution()
print(s.constructDistancedSequence(7))