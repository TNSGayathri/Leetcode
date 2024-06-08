class Solution:
    def countDigits(self, n: int) -> int:
        t=n
        c=0
        while t>0:
            r=t%10
            if(n%r==0):
                c+=1
            t=t//10
        return c