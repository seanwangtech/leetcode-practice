from typing import *
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        ret = []
        prime_numbsers = []
        count=0
        for i in range(2, right+1):
            isPrime = True
            i_2 = int(i**0.5)
            for j in prime_numbsers:
                count+=1
                if(j>i_2):
                    break
                if(i%j == 0):
                    isPrime = False
                    break
            if(isPrime): 
                prime_numbsers.append(i)
                if(i>=left):
                    ret.append(i)
        print(count)
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

