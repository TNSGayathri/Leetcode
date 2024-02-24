class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        d={}
        l=s.split()
        if(len(pattern)!=len(l)):
            return False
        # print(l)
        m=[]
        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]] != l[i]:
                    return False
                    # print(1)
            else:
                if(l[i] in m):
                    return False
                d[pattern[i]]=l[i]
                m.append(l[i])
        # print(d)
        return True
        