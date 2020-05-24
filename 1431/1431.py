from typing import List

class Solution(object):
    def kidWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        biggestEle = max(candies)
        subList = [biggestEle - i for i in candies]
        return [True if i <= extraCandies else False for i in subList]