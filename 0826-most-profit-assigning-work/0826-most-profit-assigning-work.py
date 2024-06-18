class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        d={}
        for i in range(len(difficulty)):
            if difficulty[i] not in d:
                d[difficulty[i]] = profit[i]
            else:
                d[difficulty[i]] = max(d[difficulty[i]], profit[i])
        l=sorted(d)
        worker.sort()
        # print(d,l,worker)
        if(l[0])>worker[-1]:
            return 0
        j=0
        ma=0
        tp=0
        for i in worker:
            while j<len(l) and i>=l[j]:
                ma=max(ma,d[l[j]])
                j+=1
            tp+=ma
            # print(ma)
        return tp