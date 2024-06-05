class Solution {
public:
    void dfs(int row,int col,vector<vector<int>> &image,vector<vector<int>> &ans,int drow[],int dcol[],int color,int c){
        ans[row][col]=color;
        int n=image.size();
        int m=image[0].size();
        for (int i=0;i<4;i++){
            int nrow=row+drow[i];
            int ncol=col+dcol[i];
            if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && image[nrow][ncol]==c &&ans[nrow][ncol]!=color){
                dfs(nrow,ncol,image,ans,drow,dcol,color,c);
            }
        }
    }
    vector<vector<int>> floodFill(vector<vector<int>>& image, int sr, int sc, int color) {
        int c=image[sr][sc];
        vector<vector<int>> ans=image;
        int drow[]={-1,0,1,0};
        int dcol[]={0,+1,0,-1};
        dfs(sr,sc,image,ans,drow,dcol,color,c);
        return ans;
    }
};