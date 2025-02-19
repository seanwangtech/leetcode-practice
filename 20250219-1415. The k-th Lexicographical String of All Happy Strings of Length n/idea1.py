class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = list('abc')
        ans = [""]
        count = 0
        def dfs()->bool:
            nonlocal n,k, letters, count
            if len(ans)-1 == n:
                count += 1
                if(count ==k):
                    return True
                else:
                    return False
            for i in range(3):
                chr = letters[i]
                if(ans[-1] != chr):
                    ans.append(chr)
                    isFound = dfs()
                    if isFound:
                        return True
                    ans.pop()
            return False
        
        dfs()
        return ''.join(ans)

s = Solution()
print(s.getHappyString(30, 50000))