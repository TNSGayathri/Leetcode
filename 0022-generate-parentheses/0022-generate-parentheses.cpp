class Solution {
public:
    void fun(int o,int c,int n,string &s,vector<string> &v)
    {
        if(n==o && n==c){
            v.push_back(s);
            return ;
        }
        if(n>o){
            s+="(";
            fun(o+1,c,n,s,v);
            s.pop_back();
        }
        if(o>c){
            s+=")";
            fun(o,c+1,n,s,v);
            s.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        vector<string>l;
        string s="";
        fun(0,0,n,s,l);
        return l;
    }
};