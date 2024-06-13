class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        d={}
        c=0
        for i in range(len(s)):
            d[s[i]]=i
        for i in range(len(t)):
            c+=abs(i-d[t[i]])
        return c