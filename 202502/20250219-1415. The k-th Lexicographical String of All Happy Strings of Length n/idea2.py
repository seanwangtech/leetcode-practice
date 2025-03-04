class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = list('abc')
        ans = [""]
        if(k> 3*2**(n-1)):
            return ""
        else:
            k0Based = k-1
            for i in range(n):
                quotient = k0Based// (2**(n-i-1))
                k0Based %= (2**(n-i-1))  # update k
                for i in range(3):
                    if (letters[i] != ans[-1]):
                        if(quotient == 0):
                            ans.append(letters[i])
                            break
                        quotient -= 1
                        
        return ''.join(ans)
                
s = Solution()
print(s.getHappyString(1, 3))