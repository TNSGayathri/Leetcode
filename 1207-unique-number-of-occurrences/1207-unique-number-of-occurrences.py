class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        v=list(d.values())
        s=list(set(v))
        if(len(v)==len(s)):
            return True
        return False
        