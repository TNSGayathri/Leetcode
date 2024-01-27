class Solution {
public:
    vector<vector<vector<int>>>v;
    int mod=1e9+7;
    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        
        v=vector<vector<vector<int>>>(m,vector<vector<int>>(n,vector<int>(maxMove+1,-1)));
        return fun(m,n,maxMove,startRow,startColumn);
        
    }
    int fun(int m,int n,int maxMove,int i,int j)
    {
        if(i < 0 || j<0 ||i>=m || j>=n){
            return 1;
        }
        if(maxMove<=0){
            return 0;
        }
        if(v[i][j][maxMove]!=-1){
            return v[i][j][maxMove];
        }
        int f1=0;
        f1 =(f1+fun(m,n,maxMove-1,i+1,j))%mod;
        f1=(f1+fun(m,n,maxMove-1,i-1,j))%mod;
        f1=(f1+fun(m,n,maxMove-1,i,j-1))%mod;
        f1=(f1+fun(m,n,maxMove-1,i,j+1))%mod;
        return v[i][j][maxMove]=f1;
    }
};