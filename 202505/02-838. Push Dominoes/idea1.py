class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        result = []
        pre = 'L' # no affect to the right
        ndot = 0
        for chr in dominoes:
            if chr =='.':
                ndot += 1
            else:
                if chr == 'L':
                    if pre == 'L':
                        result.extend(['L']*(ndot+1))
                    else:
                        result.extend(['R']*(ndot//2) +
                            ['.']*(ndot%2) +
                            ['L']*(ndot//2+1) 
                        )
                elif chr == 'R':
                    if pre == 'L':
                        result.extend(['.']*ndot + ['R'])
                    else:
                        result.extend([pre]*ndot + ['R'])
                pre = chr
                ndot = 0
        if pre == 'L':
            result.extend(['.']*ndot)
        else: 
            result.extend(['R']*ndot)
            
        return ''.join(result)
                

s = Solution()
print(s.pushDominoes('.L.R...LR..L..'))