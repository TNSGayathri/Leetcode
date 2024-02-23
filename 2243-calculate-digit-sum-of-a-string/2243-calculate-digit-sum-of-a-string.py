class Solution:
    def digitSum(self, s: str, k: int) -> str:
        i=0
        m=""
        def su(l):
            s=0
            for i in l:
                s+=int(i)
            return s
        while len(s)>k:
            for i in range(0,len(s),k):
                m1=s[i:i+k:]
                # print(m1)
                m+=str(su(m1))
            s=m
            m=""
            
        return s
            
            