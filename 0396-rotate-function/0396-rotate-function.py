class Solution:
    def maxRotateFunction(self, a: List[int]) -> int:
            n = len(a)
            if n == 0:
                return 0
            S = sum(i * a[i] for i in range(n))
            sum_a = sum(a)
            max_sum = S
            for i in range(1, n):
                S = S + sum_a - n * a[n - i]
                max_sum = max(max_sum, S)

            return max_sum
