class Solution:
    def sortSentence(self, s: str) -> str:
        s=s.split(" ")
        l=[0]*len(s)
        for i in s:
            l[int(i[-1])-1]=i[:len(i)-1:]
        l=" ".join(l)
        return l
        