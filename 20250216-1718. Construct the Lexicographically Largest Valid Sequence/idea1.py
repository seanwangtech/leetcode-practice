from typing import *
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        depth = 0
        maxDepth = 0
        def largestValidNum(seq:List[int], n:int):
            nonlocal depth, maxDepth
            depth += 1
            try:
                if(len(seq) == 2*n-1):
                    return seq
                for nr in range(n, 0, -1):
                    print(seq, nr)
                    if(nr == 1):
                        if(nr not in seq):
                            seq.append(nr)
                            return largestValidNum(seq, n)
                        else:
                            #no valid number options
                            return None
                    else:
                        if(nr in seq):
                            if(len(seq)>=nr and seq[-nr] == nr 
                            and seq.count(nr) == 1):
                                #valid number and start test next element
                                seq.append(nr)
                                ret = largestValidNum(seq, n)
                                if( ret ):
                                    return ret
                                else:
                                    seq.pop()       
                        else:
                            if(2*n-1 - len(seq) > nr):
                                #valid number and start test next element
                                seq.append(nr)
                                ret = largestValidNum(seq, n)
                                if( ret ):
                                    return ret
                                else:
                                    seq.pop()
                return None
            finally:
                maxDepth = max(depth, maxDepth)
                depth-=1

        ret = largestValidNum([],n)
        print("macDepth=", maxDepth)
        return ret

s = Solution()
print(s.constructDistancedSequence(5))