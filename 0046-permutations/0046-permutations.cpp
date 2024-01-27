class Solution {
public:
    void per(vector<int>&nums,vector<int>&fre,vector<int>&d,vector<vector<int>>&v){
        if(nums.size()==d.size())
        {
            v.push_back(d);
            return ;
        }
        for(int i=0;i<nums.size();i++)
        {
            if(fre[i]==0)
            {
                fre[i]=1;
                d.push_back(nums[i]);
                per(nums,fre,d,v);
        fre[i]=0;
                d.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int>fer(nums.size(),0);
        vector<int>ds;
        vector<vector<int>> v;
        per(nums,fer,ds,v);
        return v;
        
    }
};