from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

        return min(dp[-2], dp[-1])

        # 空间优化
        # n = len(cost)
        # pre, cur = cost[0], cost[1]
        # for i in range(2, n):
        #     cur, pre = min(pre, cur) + cost[i], cur
        # return min(pre, cur)

solution = Solution()
print(solution.minCostClimbingStairs([10, 15, 20]))
print(solution.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

"""
到第N级台阶有两种走法，
1). 先走到第n-1级， 然后花费cost[i]一步到达
2). 先走到第n-2级， 然后花费cost[i]两步到达

dp[n]表示到n阶的最小花费
那么就有dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
"""