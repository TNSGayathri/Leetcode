class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sl=s.split(" ")
        # print(sl)
        sl=sl[:k:]
        return " ".join(sl)
        