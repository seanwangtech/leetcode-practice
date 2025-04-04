# time complexity worst case O(n)
# space complexity: O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        NV = len(vowels)
        count = 0
        iv=0
        vowelsSeen = {}
        icl,icu = -1,0
        # position the iv
        for i in range(len(word)):
            chr = word[i]
            if chr in vowels:
                vowelsSeen[chr] = vowelsSeen.get(chr,0)+1
                if(len(vowelsSeen) == NV):
                    iv = i
                    break
        if iv == 0:
            return 0
        # position the icl, icu
        ki = k
        for i in range(len(word)):
            chr = word[i]
            if chr in vowels:
                if(ki == 0):
                    icu +=1
            else:
                ki -= 1
                if(ki == 0):
                    icl = i
                    icu = icl+1
                elif(ki < 0):
                    break
        if(k != 0 and icl == -1):
            return 0
            
        for i in range(len(word)):
            if(icu-max(icl,iv)) >=0:
                count += icu - max(icl, iv)
            chr = word[i]
            if chr in vowels:
                vowelsSeen[chr] -=1
                while(vowelsSeen[chr] ==0):
                    iv += 1
                    if iv< len(word):
                        if word[iv] in vowels:
                            vowelsSeen[word[iv]] += 1
                    else:
                        return count
            else:
                icl = icu
                if icl < len(word):
                    icu = icl+1
                    while icu<len(word) and word[icu] in vowels:
                        icu+=1
                else:
                    return count
        
        return count

s = Solution()  
print(s.countOfSubstrings(word = "aeiou", k = 0))
print(s.countOfSubstrings(word = "aeouih", k = 0))
print(s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
print(s.countOfSubstrings(word = "iqeaouqi", k = 2))
print(s.countOfSubstrings(word = "oocaeui", k = 0))
print(s.countOfSubstrings(word = "oiabueo", k = 0))
print(s.countOfSubstrings(word = "dauocinloe", k = 2))