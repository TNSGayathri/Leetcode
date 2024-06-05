class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        m=""
        j=0
        spaces.sort()
        for i in range(len(s)):
            if j<len(spaces) and i==spaces[j]:
                m+=" "+s[i]
                j+=1
            else:
                m+=s[i]
        return m
            
        