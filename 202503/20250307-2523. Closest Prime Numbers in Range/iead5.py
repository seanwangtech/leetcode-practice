from typing import *
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        nums = [True]*(right+1)
        nums[0] = False
        nums[1] = False
        count = 0
        for i in range(2, int(right**0.5)+1):
            if(nums[i]):
                for j in range(i*i, right+1, i):
                    count+=1
                    nums[j] = False
                    
        print(count)
        ret = [i for i in range(left, right+1) if nums[i]]
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

