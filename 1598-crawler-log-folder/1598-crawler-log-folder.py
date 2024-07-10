class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l=[0]
        for i in logs:
            if l==[0] and i=="../":
                continue
            elif i=="../":
                l.pop()
            elif i=="./":
                continue
            else:
                l.append(i)
        return len(l)-1