import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
            projects = list(zip(capital, profits))
    
    # Sort projects by capital requirement
            projects.sort(key=lambda x: x[0])
            max_heap = []

            i = 0
            n = len(projects)

            for _ in range(k):
                # Push all the projects we can start with the current capital to the max-heap
                while i < n and projects[i][0] <= w:
                    heapq.heappush(max_heap, -projects[i][1])  # use negative profit to simulate max-heap
                    i += 1

                # If we can't start any project, break early
                if not max_heap:
                    break

                # Pop the project with the maximum profit
                w += -heapq.heappop(max_heap)

            return w

        