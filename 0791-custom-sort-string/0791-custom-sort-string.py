class Solution:
    def customSortString(self, order: str, s: str) -> str:
        l=[]
        nl=[]
        for i in s:
            if i in order:
                l.append(i)
            else:
                nl.append(i)
        d={}
        for i in l:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        m=""
        for i in order:
            if i in d.keys():
                m+=i*d[i]
        for i in nl:
            m+=i
        return m
        