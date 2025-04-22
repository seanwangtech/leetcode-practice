from curses import nonl
from itertools import combinations
from tkinter import N


class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        freq = [0]*n
        MOD = int(1e9 + 7)
        def helper(isFirst = False, index=0, base=1):
            nonlocal freq, n, maxValue
            if index>=n or base>maxValue:
                return 
            init = base if isFirst else base*2
            for i in range(init, maxValue+1, base):
                freq[index] += 1
                helper(False, index+1, i )
        helper(True)
        ret = 0
        for i, f in enumerate(freq):
            ret += f*self.combination(n-1, i)
            ret %=MOD
        return ret
    def combination(self, n, k):
        ret = 1
        for i in range(n, n-k, -1):
            ret*= i
        for i in range(1, k+1):
            ret //= i
        return ret

            


s = Solution()
print(s.idealArrays(n = 2, maxValue = 5))
print(s.idealArrays(n = 5, maxValue = 3))