# time complexity worst case O((n-k)n)
# space complexity: O(1)
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        NV = len(vowels)
        count = 0
        for i in range(len(word)-NV+1-k):
            vowelsSeen = set()
            nCon = 0
            for j in range(i,len(word)):
                if word[j] in vowels:
                    vowelsSeen.add(word[j])
                else: 
                    nCon += 1
                if(nCon > k):
                    break
                elif(nCon == k and len(vowelsSeen) == NV):
                    count += 1
        return count
    
s = Solution()
print(s.countOfSubstrings(word = "aeiou", k = 0))
print(s.countOfSubstrings(word = "aeiou", k = 0))
# print(s.countOfSubstrings(word = "ieaouqqieaouqq", k = 1))