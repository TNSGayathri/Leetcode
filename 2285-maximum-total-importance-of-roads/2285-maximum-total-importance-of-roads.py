class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        d={}
        for i in roads:
            if i[0] in d:
                d[i[0]]+=1
            elif i[0] not in d:
                d[i[0]]=1
            if i[1] in d:
                d[i[1]]+=1
            elif i[1] not in d:
                d[i[1]]=1
        m=sorted(d.values())
        m=m[::-1]
        c=0
        k=n
        for i in m:
            c+=i*k
            k-=1
        return c