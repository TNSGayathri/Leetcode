class Solution:
    def reverseParentheses(self, s: str) -> str:
        l=[]
        for i in range(len(s)):
            if s[i]=='(':
                l.append([s[i],i])
            elif s[i]==')':
                m=l[-1][1]
                l.pop()
                s=s[:m:]+s[m:i+1:][::-1]+s[i+1::]
                
        m=""
        for i in s:
            if i !="(" and i!=")":
                m+=i
        return m