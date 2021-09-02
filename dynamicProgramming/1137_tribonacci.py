class Solution:
    def tribonacci(self, n: int) -> int:
        # dp
        # dp = [0] * (n + 1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 1
        # for i in range(3, n + 1):
        #     dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        # return dp[n]

        # dps
        if n < 2:
            return n
        if n == 2:
            return 1

        a, b, c = 0, 1, 1
        res = 0
        for i in range(3, n + 1):
            res = a + b + c
            a = b
            b = c
            c = res
        return res

s = Solution()
print(s.tribonacci(4))
print(s.tribonacci(5))
print(s.tribonacci(6))