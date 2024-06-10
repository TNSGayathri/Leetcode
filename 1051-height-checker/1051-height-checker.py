class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        m=heights[::]
        m.sort()
        c=0
        for i in range(len(heights)):
            if heights[i]!=m[i]:
                c+=1
        return c
        