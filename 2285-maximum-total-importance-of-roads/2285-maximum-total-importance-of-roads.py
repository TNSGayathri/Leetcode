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
        m = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        k=n
        for i in m:
            m[i]=k
            k-=1
        c=0
        for i in roads:
            c+=m[i[0]]+m[i[1]]
        return c