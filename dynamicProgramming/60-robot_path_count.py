class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [[1] * n] + [[1] + [0] * (n-1)] * (m - 1) #DP  
        # print(dp)
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
        # return dp[-1][-1]

        # roll DP
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]

m = 6
n = 4
solution = Solution()
print(solution.uniquePaths(m, n))