class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        j=0
        if ch not in word:
            return word
        while word[j]!=ch:
            j+=1
        return word[j:0:-1]+word[0]+word[j+1::]
        