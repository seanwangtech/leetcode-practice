class Solution:
    def smallestNumber(self, pattern: str) -> str:
        if(len(pattern)>8 or len(pattern)==0):
            return ""
        used = [False]*9 #index 0 to 8, reprent digits use or not for 1 to 9
        num = []
        def dfs(index):
            nonlocal used, num, pattern
            if(index == len(pattern)):
                return True
            for i in range(1,10,1):
                if(used[i-1]):
                    continue
                if(len(num)==0):
                    num.append(i)
                    used[i-1] = True
                    if(dfs(index)):
                        return True
                    used[i-1] = False
                    num.pop()
                else:
                    if(pattern[index]=='I'and i>num[index]) or (pattern[index]=='D'and i<num[index]) :
                        num.append(i)
                        used[i-1] = True
                        if(dfs(index+1)):
                            return True
                        used[i-1] = False
                        num.pop()
            return False
        dfs(0)
        print(num)
        return ''.join([chr(ord('0')+x) for x in num])


s = Solution()
print(s.smallestNumber("IIIDIDDD"))  