class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        m=[]
        l=[]
        for i in mat:
            m.append(i.count(1))
        for i in range(len(m)):
            j=m.index(min(m))
            l.append(j)
            m[j]=101
            
        
        return l[:k:]