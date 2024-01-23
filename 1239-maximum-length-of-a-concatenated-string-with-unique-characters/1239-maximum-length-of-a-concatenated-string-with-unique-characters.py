from itertools import combinations
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        m=[0]
        for i in range(1,len(arr)+1):
            s=list(combinations(arr,i))
            for i in s:
                l="".join(i)
                if(len(set(l))==len(l)):
                    m.append(len(l))
        return max(m)
        
            
        