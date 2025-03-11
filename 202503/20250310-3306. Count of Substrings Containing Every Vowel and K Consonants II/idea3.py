# time complexity worst case O(n)
# space complexity: O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        NV = len(vowels)
        count = 0
        iv=0
        vowelsSeen = {}
        icl,icu = -1,-1
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
        if k ==0:
            icu = 0
            for i in range(len(word)):
                chr = word[i]
                if chr in vowels:
                    icu += 1
                else:
                    break
            for i in range(len(word)):
                if(icu-iv) >=0:
                    count += icu -iv
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
                    icu = icu+1
                    while icu<len(word) and word[icu] in vowels:
                        icu += 1
                    
        else:
            for i in range(len(word)):
                chr = word[i]
                if chr in vowels:
                    if(k == 0):
                        icu +=1
                else:
                    k -= 1
                    if(k == 0):
                        icl = i
                        icu = icl+1
                    elif(k < 0):
                        break
            if(icl == -1):
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
# print(s.countOfSubstrings(word = "aeiou", k = 0))
# print(s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
# print(s.countOfSubstrings(word = "iqeaouqi", k = 2))
# print(s.countOfSubstrings(word = "oocaeui", k = 0))
# print(s.countOfSubstrings(word = "oiabueo", k = 0))
print(s.countOfSubstrings(word = "dauocinloe", k = 2))