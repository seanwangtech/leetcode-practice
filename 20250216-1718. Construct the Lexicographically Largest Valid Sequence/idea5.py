from ast import arg
from dataclasses import dataclass
from typing import *
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans:List[int] = [0]*(2*n-1)
        used:List[bool] = [False]*n
        def dfs(index=0)->bool:
            if(index == 2*n-1):
                return True
            if(ans[index] != 0):
                return dfs(index+1)
            for i in range(n, 0, -1):
                if(not used[i-1] ):
                    if(i == 1):
                        used[i-1]=True
                        ans[index] = i
                        if(dfs(index+1)):
                            return True
                        ans[index] =0
                        used[i-1]=False
                    else:
                        if index+i >= 2*n-1 or ans[index+i]!=0:
                            continue
                        used[i-1]=True
                        ans[index] = i
                        ans[index+i] = i
                        if(dfs(index+1)):
                            return True
                        ans[index+i] = 0
                        ans[index] =0
                        used[i-1]=False
            return False
                        
        dfs()
        return ans

s = Solution()
print(s.constructDistancedSequence(32))