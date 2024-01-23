class Solution {
public:
    int fib(int n) {
        if(n==0 || n==1){
            return n;
        }
        
        int sn1=fib(n-1);
        int sn2=fib(n-2);
        return sn1+sn2;
    }
};