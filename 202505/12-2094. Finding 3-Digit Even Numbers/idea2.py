from typing import *

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        freq = [0]*10
        for d in digits:
            freq[d] += 1
        result = []
        def helper(index=0, num=0):
            nonlocal freq, result
            if index== 3:
                if num >= 100 and num % 2 == 0:
                    result.append(num)
                return
            for i in range(10):
                if freq[i]>0:
                    freq[i] -= 1
                    helper(index+1, num*10+i)
                    freq[i] += 1
        helper()
        return result
            
    
s = Solution()
print(s.findEvenNumbers(digits = [2,1,3,0]))
print(s.findEvenNumbers(digits = [1,8,7,7,1,1,5,4,0,0,7,5,1,7,9]))