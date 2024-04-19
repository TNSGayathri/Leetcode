class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def land(grid,i,j,m,n):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=='0':
                return 
            grid[i][j]='0'
            land(grid,i-1,j,m,n)
            land(grid,i+1,j,m,n)
            land(grid,i,j-1,m,n)
            land(grid,i,j+1,m,n)
            
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]=="1"):
                    count+=1
                    land(grid,i,j,m,n)
        return count
        
        
        