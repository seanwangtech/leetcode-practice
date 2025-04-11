class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        i = low
        while i<=high:
            digits = []
            j = i
            while j >0:
                digits.append(j%10)
                j//=10
            
            i+=1
            if len(digits)%2 ==0:
                if(sum(digits) == 2*sum(digits[:len(digits)//2])):
                    count+=1
            else:
                i= 10**len(digits)
        return count
s = Solution()
print(s.countSymmetricIntegers(1,100))