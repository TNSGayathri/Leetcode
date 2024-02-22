class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust)==0:
            if(n==1):return 1
            else:return -1
        l=[0]*(n+1)
        for i in trust:
            l[i[0]]-=1
            l[i[1]]+=1
        for i in range(1,n+1):
            if l[i]==n-1:
                return i
        return -1