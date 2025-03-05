class Solution:
    def coloredCells(self, n: int) -> int:
        # 2*(n-1)**2 + 2*n - 1
        return 2*n**2-2*n+1
    
print(Solution().coloredCells(6))