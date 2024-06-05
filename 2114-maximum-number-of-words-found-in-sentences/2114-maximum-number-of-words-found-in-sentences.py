class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        m=[]
        for i in sentences:
            l=i.split(" ")
            m.append(len(l))
        return max(m)
        