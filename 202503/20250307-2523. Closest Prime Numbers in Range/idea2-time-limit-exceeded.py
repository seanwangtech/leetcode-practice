from typing import *
import math

class Solution:
    def __init__(self):
        self.prime_numbsers = [2]
        self.maxCalc = 2
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
        if(n>self.maxCalc):
            self.calcPrime(n)
            if(self.prime_numbsers[-1] == n):
                return True
            else:
                return False
        for i in self.prime_numbsers:
            if(i*i>n):
                break
            if(n%i == 0):
                return False
        return True
    def calcPrime(self, n):
        for i in range(self.maxCalc+1, n+1):
            isPrime = True
            for j in self.prime_numbsers:
                if(j*j>i):
                    break
                if(i%j == 0):
                    isPrime = False
                    break
            if(isPrime): 
                self.prime_numbsers.append(i)
        self.maxCalc = n
    
# print(Solution().closestPrimes(1,1000000))
# print(Solution().closestPrimes(21,25))
print(Solution().closestPrimes(937250,937331))

