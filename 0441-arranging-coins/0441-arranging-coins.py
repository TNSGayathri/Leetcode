class Solution:
    def arrangeCoins(self, n: int) -> int:
        i=0
        c=1
        while n>=0:
            n-=c
            c=c+1
            if(n<0):
                return i
            i+=1
            # print(n,c,i)
        return i