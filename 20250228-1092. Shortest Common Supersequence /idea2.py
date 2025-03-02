class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        dp = [['']*(len(str2)+1) for _ in (range(len(str1)+1))]
        for i in range(len(str1)+1):
            for j in range(len(str2)+1):
                if i==0:
                    dp[i][j] = str2[:j]
                elif j==0:
                    dp[i][j] = str1[:i]
                else:
                    if str1[i-1] == str2[j-1]:
                        dp[i][j] = dp[i-1][j-1]+str1[i-1]
                    else:
                        if len(dp[i-1][j]) < len(dp[i][j-1]):
                            dp[i][j] = dp[i-1][j]+str1[i-1]
                        else:
                            dp[i][j] = dp[i][j-1]+str2[j-1]
        print(dp)
        return dp[len(str1)][len(str2)]
s = Solution()
print(s.shortestCommonSupersequence('abac','cab'))