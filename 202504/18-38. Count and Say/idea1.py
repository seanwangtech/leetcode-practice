class Solution:
    def countAndSay(self, n: int) -> str:
        ret = '1'
        for i in range(n-1):
            ret = self.rle(ret)
        return ret

    def rle(self, s):
        if len(s) ==0:
            return ''
        preChar = s[0]
        count = 0
        arr = []
        for chr in s:
            if preChar==chr:
                count += 1
            else:
                arr.append(str(count))
                arr.append(preChar)
                preChar = chr
                count =1
        arr.append(str(count))
        arr.append(preChar)
        return ''.join(arr)

s = Solution()
print(s.countAndSay(4))