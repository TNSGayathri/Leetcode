class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        l=[]
        for i in s:
            l.append(i)
        i=0
        j=len(l)-1
        while i<j:
            if(l[i]!=l[j]):
                l[i]=min(l[i],l[j])
                l[j]=min(l[i],l[j])
            i+=1
            j-=1
        s="".join(l)
        return s
            