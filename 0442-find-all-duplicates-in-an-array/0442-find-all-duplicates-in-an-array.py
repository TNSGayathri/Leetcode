class Solution:
    def findDuplicates(self, arr: List[int]) -> List[int]:
        l=[]
        d={}
        for i in arr:
            if i not in d:
                d[i]=1
            else:
                if i not in l:
                    l.append(i)
        return l
                
        