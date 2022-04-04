class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        #inialize all positions to infinity
        res = [[float(inf)] * (cols+1) for r in range(rows+1)]
        
        #initialize one spot to zero to make the math work out
        res[rows-1][cols] = 0
        
        #iterate through the grid starting from the bottom corner
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                #add the actual value in the grid to the minimum of the below value and right value to get cost
                res[r][c]=grid[r][c] + min(res[r+1][c], res[r][c+1])
        #return top left value
        return res[0][0]
                
