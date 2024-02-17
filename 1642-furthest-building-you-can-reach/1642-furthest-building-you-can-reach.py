class Solution(object):
    def furthestBuilding(self, h, b, l):
        """
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        heap=[]
        for i in range(len(h)-1):
            d=h[i+1]-h[i]
            if d<=0:
                continue
            b-=d
            heapq.heappush(heap,-d)
            if b<0:
                if l==0:
                    return i
                l-=1
                b+=-heapq.heappop(heap)
        return len(h)-1
                    
                    
        