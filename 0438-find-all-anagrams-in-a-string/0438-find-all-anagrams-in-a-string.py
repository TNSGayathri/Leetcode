class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        m=sorted(p)
        k=len(p)
        l=[]
        for i in range(len(s)-k+1):
            m1=sorted(s[i:i+k])
            # print(m1,m)
            if(m1==m):
                l.append(i)
        return l
        