'''
给你一个整数数组 cost ，其中 cost[i] 是从楼梯第 i 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 0 或下标为 1 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。
'''

'''
输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。
'''

from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) <= 2:
            return min(cost)
        
        dp = [cost[0], cost[1]]
        for i in range(2, len(cost)):
            dp.append(min(dp[i-1], dp[i-2]) + cost[i])
        
        return min(dp[-2], dp[-1])
    
s = Solution()
print(s.minCostClimbingStairs([10, 15, 20]))
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# memory optimized
class MemoryOptimized:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        pre, cur = cost[0], cost[1]
        for i in range(2, len(cost)):
            cur, pre = min(pre, cur) + cost[i], cur
        return min(pre, cur)

mos = MemoryOptimized()
print(mos.minCostClimbingStairs([10, 15, 20]))
print(mos.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

'''
探寻python 双赋值的顺序 即
cur, pre = min(pre, cur), cur执行顺序

结果来看等效于
tmp = cur
cur = min(pre, cur)
pre = tmp

>>> a = 1
>>> b= 1
>>> id(a) 
140728380757776
>>> id(b) 
140728380757776
>>> a, b = b + 1, a
>>> a
2
>>> b
1
>>> id(a) 
140728380757808
>>> id(b) 
140728380757776
>>> c = 2 
>>> d = 3
>>> id(c) 
140728380757808
>>> id(d) 
140728380757840
>>> c, d = d + 1, c
>>> c, d
(4, 2)
>>> id(c) 
140728380757872
>>> id(d)
140728380757808
...
>>> id(d)
140728380757904
>>> e = d
>>> id(e) 
140728380757904

可以看出如果不同变量赋予同一个值, python只是将变量指向同一个内存地址
进行交换赋值之后, 只是指针指向了新的值.即python的赋值只是变量指向内存地址
'''

