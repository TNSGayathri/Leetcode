class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        m=[]
        for i in letters:
            if i >target:
                m.append(i)
        if m==[]:
            return letters[0]
        m.sort()
        return m[0]