class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j] and s!="":
            if(s[i]==s[i+1]):
                i+=1
            if(s[j]==s[j-1]):
                j-=1
            elif(s[i]!=s[i+1]and s[j]!=s[j-1]):
                s=s[i+1:j:]
                i=0
                j=len(s)-1
        if(len(s)==1):
            return 1
        if(s[0]==s[-1]):
            return 0
        return len(s)
            
            
        