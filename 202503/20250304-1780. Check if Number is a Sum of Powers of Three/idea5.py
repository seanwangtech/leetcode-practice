# Ternary Representation
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n>0:
            if n%3 == 2:
                return False
            n //=3
        return True
                
s = Solution()
print(s.checkPowersOfThree(6378022))