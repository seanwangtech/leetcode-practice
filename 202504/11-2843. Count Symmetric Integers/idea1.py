class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high+1):
            digits = []
            while i >0:
                digits.append(i%10)
                i//=10
            if len(digits)%2 ==0:
                if(sum(digits) == 2*sum(digits[:len(digits)//2])):
                    count+=1
        return count
s = Solution()
print(s.countSymmetricIntegers(1,100))