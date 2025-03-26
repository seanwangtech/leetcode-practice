from typing import *

# prefix sum and suffix sum
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
        prefix_sum = 0
        # suffix_sum = sum - arr[0]
        ret = float('inf')
        for i in range(0, M*N):
            prefix_sum += arr[i]
            suffix_sum = sum - prefix_sum
            left_op = arr[i]*(i+1) - prefix_sum
            right_op = suffix_sum - arr[i]*(M*N - (i+1))
            op = left_op + right_op
            if(op <= ret):
                ret = op
            else:
                return ret
        return ret
            
    
s = Solution()
print(s.minOperations(grid = [[2,4],[6,8]], x = 2))
print(s.minOperations(grid = [[529,529,989],[989,529,345],[989,805,69]], x = 92))