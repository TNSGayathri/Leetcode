class Solution:
    def pivotInteger(self, n: int) -> int:
        s=0
        l=[]
        m=[]
        for i in range(1,n+1):
            s+=i
            l.append(s)
        s=0
        for j in range(n,0,-1):
            s+=j
            m.append(s)
        m=m[::-1]
        for i in range(n):
            if(l[i]==m[i]):
                return i+1
        return -1