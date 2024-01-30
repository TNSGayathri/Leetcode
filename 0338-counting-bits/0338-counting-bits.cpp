class Solution {
public:
    void fun(int i,int n,vector<int>&l)
    { int c=0;
     int t=i;
        if(n+1==t){
            return;
        }
        while(i>0){
            if(i&1){
                c+=1;
            }
            i=i>>1;
        }
     l.push_back(c);
     fun(t+1,n,l);
    }
    vector<int> countBits(int n) {
        vector<int>l;
        fun(0,n,l);
        return l;
    }
};