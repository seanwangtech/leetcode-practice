class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        suffix = int(s)
        suffix_10 = 10**len(s)
        result = 0
        if start % suffix_10 > suffix and (start//suffix_10)%10<=limit:
            result -= 1
        if finish%suffix_10>= suffix and (finish//suffix_10)%10<=limit:
            result += 1
        finish //= suffix_10 
        start //= suffix_10 
        scale = 1
        while finish !=0:
            finish_reminder = min (finish % 10, limit+1)
            start_reminder = min (start % 10, limit+1)
            result += (finish_reminder - start_reminder)*scale
            scale *= (limit+1)
            finish //= 10
            start //= 10
        return result


s = Solution()
print(s.numberOfPowerfulInt(start = 1, finish = 6000, limit = 4, s = "124"))
print(s.numberOfPowerfulInt(start = 10, finish = 1844, limit = 5, s = "12"))