# time complexity worst case O(n)
# space complexity: O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        NV = len(vowels)
        ikc = -1 if k>0 else 0
        ikcn = 0
        if(ikc == 0):
            while ikc + ikcn < len(word) and word[ikc+ikcn] in vowels:
                ikcn +=1
        i5v = -1
        vowelsSeen = {}
        count = 0
        for i in range(len(word)):
            chr = word[i]
            if(chr in vowels):
                if len(vowelsSeen) ==0:
                    i5v = i
                vowelsSeen[chr] = vowelsSeen.get(chr,0)+1
                if(len(vowelsSeen) == NV):
                    while True:
                        chr1 = word[i5v]
                        if chr1 not in vowels:
                            i5v += 1
                            continue
                        if vowelsSeen[chr1] >1:
                            i5v += 1
                            vowelsSeen[chr1] -= 1
                        else:
                            break
                
            else:
                if ikc == -1:
                    if k > 1:
                        k -= 1
                    else:
                        ikc = 0
                        ikcn = 0
                        while ikc + ikcn < len(word) and word[ikc+ikcn] in vowels:
                            ikcn +=1
                else:
                    ikc += ikcn + 1
                    ikcn = 0
                    while ikc + ikcn < len(word) and word[ikc+ikcn] in vowels:
                        ikcn +=1
            if ikc >=0 and len(vowelsSeen)==NV and ikc<=i5v:
                count+= min(ikcn,i5v-ikc) +1
        return count
    
s = Solution()
print(s.countOfSubstrings(word = "aeiou", k = 0))
# print(s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))
# print(s.countOfSubstrings(word = "iqeaouqi", k = 2))
print(s.countOfSubstrings(word = "oocaeui", k = 0))