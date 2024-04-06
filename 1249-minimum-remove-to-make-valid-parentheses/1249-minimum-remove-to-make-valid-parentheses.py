class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        l=[]
        m=[]
        k=""
        for i in range(len(s)):
            m=[]
            if(s[i]=='('):
                m.append(s[i])
                m.append(i)
                l.append(m)
            elif(l and s[i]==')'):
                if(l[-1][0]=='('):
                    l.pop()
                else:
                    m.append(s[i])
                    m.append(i)
                    l.append(m)
            elif(l==[] and s[i]==')'):
                 m.append(s[i])
                 m.append(i)
                 l.append(m)
        m=[]
        for i in range(len(l)):
            m.append(l[i][1])
        for i in range(len(s)):
            if i not in m:
                k+=s[i]
        return k
                
        