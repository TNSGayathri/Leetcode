class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m=sorted(p)
        k=len(p)
        l=[]
        for i in range(len(s)-k+1):
            if(sorted(s[i:i+k])==m):
                l.append(i)
        return l
        