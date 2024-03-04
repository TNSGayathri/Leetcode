class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        i=0
        j=len(tokens)-1
        if(tokens==[]):
            return 0
        if(tokens[0]>power):
            return 0
        s=0
        while i!=j:
            if(power>=tokens[i]):
                power-=tokens[i]
                s+=1
                i+=1
            elif(power<tokens[i]):
                s-=1
                power+=tokens[j]
                j-=1
        if(power>=tokens[i]):
            s+=1
        return s