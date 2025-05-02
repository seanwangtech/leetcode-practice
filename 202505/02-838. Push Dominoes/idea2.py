class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        result = []
        forceR_L = [0]*N
        pre = 'L' 
        count = 0
        for i in range(N):
            chr = dominoes[i]
            if chr == '.':
                count += 1
                if pre == 'R':
                    forceR_L[i] += N-count
            else:
                count = 0
                pre = chr
        pre = 'R'
        count = 0
        for i in range(N-1, -1, -1):
            chr = dominoes[i]
            if chr == '.':
                count += 1
                if pre == 'L':
                    forceR_L[i] += -N + count
            else:
                count = 0
                pre = chr
        for i in range(N):
            chr = dominoes[i]
            if chr == '.':
                if forceR_L[i]>0:
                    #close to R
                    result.append('R')
                elif forceR_L[i] == 0:
                    result.append('.')
                else:
                    result.append('L')

            else:
                result.append(chr)
        return ''.join(result)

s = Solution()
print(s.pushDominoes('.L.R...LR..L..'))