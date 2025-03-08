from typing import *
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ret = []
        nums = [1]*(right+1)
        nums[0] = 0
        nums[1] = 0
        for i in range(2, right+1):
            if(nums[i] == 0):
                continue
            j = i*2
            while(j< right+1):
                nums[j] = 0
                j +=i
            if(i>=left):
                ret.append(i)
        if len(ret) <2:
            return [-1,-1]
        
        index = 0
        gap = ret[1]-ret[0]
        for i in range(1,len(ret)-1):
            gapi = ret[i+1] - ret[i]
            if(gapi < gap):
                index = i
                gap = gapi
        return ret[index:index+2]
    
# print(Solution().closestPrimes(1,1000000))
# print(Solution().closestPrimes(21,25))
print(Solution().closestPrimes(937250,937331))

