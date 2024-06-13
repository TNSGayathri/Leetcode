class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d={" ":" "}
        k=0
        for i in key:
            if i not in d:
                d[i]=chr(97+k)
                k+=1
        s=""
        for i in message:
            s+=d[i]
        return s
            