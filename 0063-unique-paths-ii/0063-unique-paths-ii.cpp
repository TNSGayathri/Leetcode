class Solution {
public:
    int vect(int i,int j,int m,int n,vector<vector<int>> &a,vector<vector<int>> &dp){
        if(i==m-1 && j==n-1){
            if(a[i][j]==1){
                return 0;
            }
            
            return 1;
        }
        if(i >= m || j >= n) return 0;
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        if(a[i][j]==1){
            return 0;
        }
        return dp[i][j]=vect(i+1,j,m,n,a,dp)+vect(i,j+1,m,n,a,dp);
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        int m=obstacleGrid.size();
        int n=obstacleGrid[0].size();
        vector<vector<int>>dp(m,vector<int>(n,-1));
        return vect(0,0,m,n,obstacleGrid,dp);
        
        
    }
};