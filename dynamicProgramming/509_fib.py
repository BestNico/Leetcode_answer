""" 迭代解法

1. 找到边界值
    本体边界值为0和1
    if n == 0 or n == 1:
        return n

2. f(n) = f(n-1) + f(n-2)

"""
class IterationSolution:
    def fib(self, n: int) -> int:
        if n ==0 or n == 1:
            return n

        return self.fib(n-1) + self.fib(n-2)
        # df = [0, 1] + [0] * (n - 1)
        # for i in range(2, n + 1):
        #     df[i] = df[i - 1] + df[i - 2]
        
        # return df[-1]

s = IterationSolution()
print(s.fib(4))


''' 动态规划 '''
'''
    第0步：最重要的，你要确定该题是否适合使用动态规划
    1. 动态规划是解决具有重叠子问题的特殊分治。要明确各个条件是否成立
    2. 回想该问题如果使用暴力解法如何求解：
        F(n)要去求解F(n-1)和F(n-2)  F(n-1)要去求解F(n-2)和F(n-3)  可以发现F(n-2)便是重复子问题  
    3. 判断可以使用动态规划来解决
'''
'''
    第一步：dp数组及下标含义:
    回想，动态规划的本质是自底向上解决重复子问题的过程，所以，dp数组要保存的也是子问题的值，这样，当上游需要子问题的答案时，可以直接查询到。
    所以，此题，dp[i]表示下标为i的位置，即F(n)中n为i时，F的值
'''
'''
    第二步：递推公式：
    dp[i]=dp[i-1]+dp[i-2]
'''
''''
    第三步：初始化dp数组
    由第二步可以看出，0和1是必须初始化的，其余无所谓
'''

class DPSolution:
    def fib(self, n: int) -> int:
        ''' fib '''
        if n == 0 or n == 1:
            return n
        
        dp = [0, 1]
        for i in range(2, n+1):
            dp.append(dp[i-1] + dp[i-2])
        
        return dp[n]

s = DPSolution()
print(s.fib(5))