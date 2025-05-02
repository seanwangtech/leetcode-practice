class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N = len(dominoes)
        result = []
        force = [0]*N
        f = 0
        for i in range(N):
            chr = dominoes[i]
            if chr == 'L':
                f = 0
            elif chr == 'R':
                f = N
            else:
                if f>0:
                    f = f-1
            force[i] += f
        
        for i in range(N-1, -1, -1):
            chr = dominoes[i]
            if chr == 'L':
                f = N
            elif chr == 'R':
                f = 0
            else:
                if f>0:
                    f = f-1
            force[i] -= f
        
        for f in force:
            if f>0:
                result.append('R')
            elif f ==0:
                result.append('.')
            else:
                result.append('L')
        return ''.join(result)

s = Solution()
print(s.pushDominoes('.L.R...LR..L..'))