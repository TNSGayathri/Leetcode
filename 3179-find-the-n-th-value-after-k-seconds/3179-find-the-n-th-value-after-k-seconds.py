class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        mod=1e9+7
        l=[1]*n
        c=0
        while c<k:
            s=1
            m=[1]
            for i in range(1,n):
                s+=int(l[i]%mod)
                m.append(s)
            l=m
            c+=1
        # print(l)
        return int(l[-1]%mod)
                
                
            
            