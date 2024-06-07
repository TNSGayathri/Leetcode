class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d={}
        for i in s:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for i in t:
            if i not in d:
                return i
            else:
                if(d[i]==0):
                    return i
                d[i]-=1
            
        
        