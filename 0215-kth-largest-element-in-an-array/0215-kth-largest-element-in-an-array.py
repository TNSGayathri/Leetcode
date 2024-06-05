import heapq as hq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h= []
        for i in nums:
            hq.heappush(h, i)
            if len(h) > k:
                hq.heappop(h)
        return hq.heappop(h)