class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        d={}
        for i in range(len(word)):
            if word[i].isupper():
                d[i]=word[i]
        # print(d)
        if(len(d)==1):
            l=list(d.keys())
            if(l==[0]):
                return True
            return False
        if(len(d)==len(word)or len(d)==0):
            return True
        return False
                
        