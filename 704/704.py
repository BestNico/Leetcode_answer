"""
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] == target:
                return mid
            else:
                left = mid + 1
        
        return -1

s = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(s.search(nums, target))
