class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def helper(n,x=0):
            if(n==0):
                return True
            if(n<3**x): 
                return False
            return helper(n-3**x, x+1) or helper(n, x+1)
        return helper(n)
s = Solution()
print(s.checkPowersOfThree(6378022))