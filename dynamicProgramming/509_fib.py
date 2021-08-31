class Solution:
    def fib(self, n: int) -> int:
        if n ==0 or n == 1:
            return n
        df = [0, 1] + [0] * (n - 1)
        for i in range(2, n + 1):
            df[i] = df[i - 1] + df[i - 2]
        
        return df[-1]

s = Solution()
print(s.fib(4))