'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？ 
'''

'''
输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶
'''

'''
思路分析；
    想要到n阶台阶时候
    可以选择从n-1阶迈一阶台阶到n阶
    or
    也可以选择从n-2阶迈两阶台阶到n阶
    
边界值:
    n = 0 return 0
    n = 1, 2 return 1, 2

dp数组 [0, 1, 2]
i表示到i阶台阶有几种方法
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        dp = [0, 1, 2]
        for i in range(3, n + 2):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]

s = Solution()
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))