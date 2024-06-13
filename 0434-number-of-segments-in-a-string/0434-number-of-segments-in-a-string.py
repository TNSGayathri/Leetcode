class Solution:
    def countSegments(self, s: str) -> int:
        if(s==""):
            return 0
        l=s.split()
        # while i>0:
        #     l.remove(" ")
        #     i-=1
        # print(l)
        return len(l)