class Solution:
    def secondHighest(self, s: str) -> int:
        l=[]
        for i in s:
            if i.isdigit():
                l.append(int(i))
        l=list(set(l))
        l.sort()
        if(len(l)<2):
            return -1
        return l[-2]