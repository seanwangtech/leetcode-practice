class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if(len(str1)< len(str2)):
            str1,str2 = str2, str1
        # middle match
        if(str2 in str1):
            return str1
        # left match
         
        for i in range(len(str2)-1):
            o = len(str2)-i-1 # number of overlapping letters to test
            if self.isSubStr(str1,str2[-o:]):
                #left match
                return str2[:-o]+str1
            if self.isSubStr(str1,str2[:o]):
                #right match
                return str1 + str2[o:]
        return str1 + str2
    def isSubStr(self,str1, substr) -> bool:
        i = 0
        for chr in str1:
            if(substr[i] == chr):
                i+=1
            if(i == len(substr)):
                return True
        return False
s = Solution()
print(s.shortestCommonSupersequence("bbababbb","bbbaaaba"))