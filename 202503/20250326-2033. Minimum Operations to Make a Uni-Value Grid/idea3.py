from typing import *

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        M = len(grid)
        N = len(grid[0])
        reminder = grid[0][0]%x
        arr = []
        sum = 0
        for row in grid:
            for num in row:
                sum += num//x
                arr.append(num//x)
                if num % x != reminder:
                    return -1
        arr.sort()
        ret = count = sum - arr[0]*M*N
        for i in range(1, M*N):
            diff = arr[i] - arr[i-1]
            leftN = i
            rightN = M*N -(i)
            count = diff*leftN - diff*rightN + count
            if(count <= ret):
                ret = count
            else:
                return ret
        return ret
            
    
s = Solution()
print(s.minOperations(grid = [[2,4],[6,8]], x = 2))
print(s.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92))