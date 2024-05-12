class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l=[]
        for i in range(1,max(arr)+1):
            if i not in arr:
                l.append(i)
        if(len(l)<k):
            return arr[-1]+abs((len(l)-k))
        return l[k-1]
            
        