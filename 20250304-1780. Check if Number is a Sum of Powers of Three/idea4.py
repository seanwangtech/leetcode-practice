import math
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        for i in range(int(math.log(n,3)),-1,-1):
            xp3 = 3**i
            if(n > xp3):
                n = n - 3**i
            elif(n == xp3):
                return True
        return False
                
s = Solution()
print(s.checkPowersOfThree(6378022))