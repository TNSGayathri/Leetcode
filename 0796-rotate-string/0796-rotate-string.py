class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        c=1
        m=len(s)
        while c<m:
            a=s[-1]
            s=a+s[:-1:]
            if(s==goal):
                return True
            c+=1
        return False
            
            