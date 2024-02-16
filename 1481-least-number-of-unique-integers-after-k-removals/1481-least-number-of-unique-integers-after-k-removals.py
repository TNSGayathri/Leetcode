class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        d={}
        c=0
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        l.sort()
        i=0
        while k>0:
            m=l[i]
            if(m==1):
                l[i]=0
                i+=1
            else:
                l[i]=m-1
            k-=1
        # print(l)
        for i in range(len(l)):
            if(l[i]!=0):
                c+=1
        return c
