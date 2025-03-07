from typing import *
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ret = []
        for n in range(left, right+1):
            if(self.isPrime(n)):
                ret.append(n)
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
    
    def isPrime(self, n):
        if n <2: 
            return False
        ns = int(math.sqrt(n))
        for i in range(2, ns+1):
            if(n%i == 0):
                return False
        return True
    
# print(Solution().closestPrimes(10,19))
# print(Solution().closestPrimes(1,1000000))
print(Solution().closestPrimes(937250,937331))