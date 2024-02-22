class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if(n==1):return 1
            else:return -1
        l=[]
        l1=[]
        m=[]
        for i in trust:
            l.append(i[0])
            l1.append(i[1])
        for i in l1:
            if i not in l:
                m.append(i)
        # print(l,m)
        if(len(set(l))==len(m)):
            return m[0]
        return -1
        