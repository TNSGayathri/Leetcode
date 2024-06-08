class Solution:
    def numberOfMatches(self, n: int) -> int:
        if(n==1):
            return 0
        s=0
        while n>2:
            s+=(n//2)
            if(n%2==0):
                n=n//2
            else:
                n=(n//2)+1
        return s+1