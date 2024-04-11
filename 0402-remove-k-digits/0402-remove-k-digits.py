class Solution:
    def removeKdigits(self, s: str, k: int) -> str:
        l=[]
        for i in s:
            while k>0 and l and l[-1]>i:
                k-=1
                l.pop()
            l.append(i)
        
        m=[]
        if k==0:
            for j in l:
                m.append(j)
            
        else:
            for k in range(len(l)-k):
                m.append(l[k])
        s="".join(m).lstrip("0")
        if(s!=""):
            return s
        return "0"
        