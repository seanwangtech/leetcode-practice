from typing import *
import heapq

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        N = len(nums)
        numMax = max(nums)
        primeScore = [0]*(numMax+1)
        buff = list(range(0, numMax+1))
        for i in range(2, numMax+1):
            num = buff[i]
            if num>1:
                for j in range(i, numMax+1, i):
                    while buff[j]%num == 0:
                        buff[j] //= num
                    primeScore[j] += 1

        numsPrimeScore = [primeScore[x] for x in nums]
        print(numsPrimeScore)
        numsiHeap = [(-x,i) for i,x in enumerate(nums)]
        heapq.heapify(numsiHeap)
        ret = 1
        MOD = int(10e9 + 7)
        while k>0:
            num, i = heapq.heappop(numsiHeap)
            num = -num
            left = right = 0
            j = i-1
            while j>=0 and numsPrimeScore[j] < numsPrimeScore[i]:
                j-=1
                left += 1
            j = i+1
            while j<N and numsPrimeScore[j] <= numsPrimeScore[i]:
                j+=1
                right += 1
            numOfSubArrays = (left+1)*(right+1)
            while k>0 and numOfSubArrays>0:
                k -= 1
                numOfSubArrays -= 1
                ret *= num
                ret %= MOD
        return ret


s = Solution()
print(s.maximumScore(nums = [8,3,9,3,8], k = 2))
print(s.maximumScore(nums = [19,12,14,6,10,18], k = 3))

