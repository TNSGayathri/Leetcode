class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i not in d.keys():
                d[i]=1
            else:
                d[i]+=1
        l=list(d.values())
        l.sort()
        l=l[-k::]
        m=[]
        for i in d:
            if d[i] in l:
                m.append(i)
        return m