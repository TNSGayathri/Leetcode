class Solution:
    def climbStairs(self, n: int) -> int:
        t1=1
        t2=1
        if(n==1):
            return t1
        c=1
        while c<n:
            t3=t1+t2
            t1=t2
            t2=t3
            c+=1
        return t3
        