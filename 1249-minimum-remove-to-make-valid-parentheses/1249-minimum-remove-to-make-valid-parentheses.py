class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l=[]
        k=""
        for i in range(len(s)):
            if(s[i]=='('):
                l.append([s[i],i])
            elif(l and s[i]==')'):
                if(l[-1][0]=='('):
                    l.pop()
                else:
                    l.append([s[i],i])

            elif(l==[] and s[i]==')'):
                 l.append([s[i],i])
        m=[]
        for i in range(len(l)):
            m.append(l[i][1])
        for i in range(len(s)):
            if i not in m:
                k+=s[i]
        return k
                
        