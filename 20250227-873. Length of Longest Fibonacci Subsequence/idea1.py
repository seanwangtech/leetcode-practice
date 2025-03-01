from typing import *

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        result = 0

        for i in range(0, len(arr)-2):
            for j in range(i+1, len(arr)-1):
                a,b = arr[i],arr[j]
                result = max(result, self.fibLen(a,b,s))
        if(result<3):
            return 0
        return result


    def fibLen(self, a,b,s:Set[int]):
        count =2 
        while True:
            a,b = b, a+b
            if b in s:
                count+=1
            else:
                return count

s = Solution()
print(s.lenLongestFibSubseq([1,2,3,4,5,6,7,8]))