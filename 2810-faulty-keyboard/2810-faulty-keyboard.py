class Solution:
    def finalString(self, s: str) -> str:
        s1=""
        for i in s:
            if i =="i":
                s1=s1[::-1]
            else:
                s1+=i
        return s1
            