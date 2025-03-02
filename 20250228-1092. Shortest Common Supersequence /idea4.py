# time complexity: O(len(str1)**2*len(str2)**2)
# space complexity: O(min{len(str1),len(str2)}*len(str1)*len(str2))

class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if(len(str1)<len(str2)):
            #optimize memory
            str1,str2 = str2,str1
        dp = [['']*(len(str2)+1) for _ in range(2)]
        for i in range(len(str1)+1):
            i_cur = i%2
            i_pre = (i-1)%2
            for j in range(len(str2)+1):
                if i==0:
                    dp[i_cur][j] = str2[:j]
                elif j==0:
                    dp[i_cur][j] = str1[:i]
                else:
                    if str1[i-1] == str2[j-1]:
                        dp[i_cur][j] = dp[i_pre][j-1]+str1[i-1]
                    else:
                        if len(dp[i_pre][j]) < len(dp[i_cur][j-1]):
                            dp[i_cur][j] = dp[i_pre][j]+str1[i-1]
                        else:
                            dp[i_cur][j] = dp[i_cur][j-1]+str2[j-1]
        print(dp)
        return dp[i_cur][len(str2)]
s = Solution()
print(s.shortestCommonSupersequence('abac','cab'))