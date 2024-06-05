class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        d={}
        for i in range(len(words[0])):
            if words[0][i] not in d:
                d[words[0][i]]=1
            else:
                d[words[0][i]]+=1
            
        for i in range(1,len(words)):
            k={}
            for j in words[i]:
                if j not in k:
                    k[j]=1
                else:
                    k[j]+=1
            
            for l in d.keys():
                if l in k.keys():
                    d[l]=min(d[l],k[l])
                else:
                    d[l]=0
        m=[]
        for i in d.keys():
            if d[i]!=0:
                while d[i]>0:
                    m.append(i)
                    d[i]-=1
                
        return m
        