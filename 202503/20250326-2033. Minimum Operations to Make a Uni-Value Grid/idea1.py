from typing import *

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M = len(grid)
        N = len(grid[0])
        sum = 0
        reminder = grid[0][0]%x
        for row in grid:
            for num in row:
                sum += num//x
                if num % x != reminder:
                    return -1
        
        avg = sum//(M*N)
        count1, count2 = self.countOp(grid, x, avg), self.countOp(grid, x, avg+1)
        if(count1 < count2):
            avg -= 1
            count2 = self.countOp(grid, x, avg)
            while(count1 > count2):
                avg -= 1
                count1 = count2
                count2 = self.countOp(grid, x, avg)
            return count1
        else:
            avg += 2
            count1 = count2
            count2 = self.countOp(grid, x, avg)
            while(count1 > count2):
                avg += 1
                count1 = count2
                count2 = self.countOp(grid, x, avg)
            return count1
        
        return min(count)
    def countOp(self, grid, x, target):
        count = 0
        for row in grid:
            for num in row:
                count += abs(num//x - target )
        return count
    
s = Solution()
print(s.minOperations(grid = [[2,4],[6,8]], x = 2))
print(s.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92))