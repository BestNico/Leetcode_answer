class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0 or n == 1: return n
        # a = b = 1
        # for i in range(2, n + 1):
        #     a, b = b, a + b
        # return b
        if n == 0 or n == 1: return n
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]

s = Solution()
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))