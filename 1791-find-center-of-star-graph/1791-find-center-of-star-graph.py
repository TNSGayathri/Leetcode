class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d={}
        ma=0
        for i in edges:
            if i[0] in d:
                d[i[0]]+=1
            else:
                d[i[0]]=1
            if i[1] in d:
                d[i[1]]+=1
            else:
                d[i[1]]=1
        for i in d.keys():
            if(ma<d[i]):
                ma=i
        return ma
            