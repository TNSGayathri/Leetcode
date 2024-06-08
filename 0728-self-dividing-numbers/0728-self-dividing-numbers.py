class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def sel(n):
            t=n
            c=0
            while t>0:
                r=t%10
                if(r !=0 and n%r==0):
                    c+=1
                t=t//10
            return c
            
        l=[]
        for i in range(left,right+1):
            if(sel(i)==len(str(i))):
                l.append(i)
        return l