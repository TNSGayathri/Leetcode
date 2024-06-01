class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s=len(strs)
        if s==0:
            return " "
        if s==1:
            return strs[0]
        strs.sort()
        a=min(len(strs[0]),len(strs[s-1]))
        i=0
        while (i<a and strs[0][i]==strs[s-1][i]):
            i+=1
        pre=strs[0][0:i]
        return pre