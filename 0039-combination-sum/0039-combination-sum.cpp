class Solution {
public:
    vector<vector<int>>comb(int i,int n,int k,vector<int>&cm,vector<vector<int>>&v,vector<int>&a)
    {
        if(i==n){
            if(k==0)
            {
                v.push_back(cm);
            }
            return v ;
        }
        if(a[i]<=k){
            cm.push_back(a[i]);
            k-=a[i];
            comb(i,n,k,cm,v,a);
            k+=a[i];
            cm.pop_back();
        }
        comb(i+1,n,k,cm,v,a);
        return v;
    }
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<vector<int>>v;
        vector<int>cm;
        int n=candidates.size();
        comb(0,n,target,cm,v,candidates);
        
        return v;
    }
};