class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        d={}
        for i in meetings:
            if i[0] not in d:
                d[i[0]]=i[1]
            else:
                d[i[0]]=max(d[i[0]],i[1])
        
        s=sorted(d)
        m=s[0]
        c=0
        for i in s:
            if m<i:
                c+=(i-m-1)
                m=i
            if(m<d[i]):
                m=d[i]
        
        return c+(days-m)+(s[0]-1)
        