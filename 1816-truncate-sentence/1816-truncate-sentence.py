class Solution:
    def truncateSentence(self, s: str, m: int) -> str:
        k=""
        c=0
        for i in s:
            if(c==m-1 and i==" "):
                return k  
            if(c<m):
                k+=i
            if i==" ":
                c+=1
            # print(k)
            
        return k
        