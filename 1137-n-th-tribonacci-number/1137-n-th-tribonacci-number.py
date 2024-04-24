class Solution:
    def tribonacci(self, n: int) -> int:
        t=0
        t1=1
        t2=1
        if(n==0):
            return t
        elif(n==1 or n==2):
            return t1
        n=n-2
        while n>0:
            t3=t+t1+t2
            t=t1
            t1=t2
            t2=t3
            n-=1
        return t3
        
        