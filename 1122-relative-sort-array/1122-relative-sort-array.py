class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d={}
        arr1.sort()
        for i in arr1:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        l=[]
        for i in arr2:
            while d[i]>0:
                l.append(i)
                d[i]-=1
        for i in d:
            while d[i]>0:
                l.append(i)
                d[i]-=1
        print(d)
        return l